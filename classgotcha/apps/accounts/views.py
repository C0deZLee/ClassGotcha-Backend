import uuid, re
from django.utils import timezone
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from django.core.files.base import File
from django.contrib.auth.hashers import check_password

from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..classrooms.serializers import Classroom, BasicClassroomSerializer
from ..posts.serializers import Moment, MomentSerializer, NoteSerializer, Comment, CommentSerializer
from ..chatrooms.serializers import ChatroomSerializer
from ..tasks.serializers import TaskSerializer

from ..posts.models import Rate
from models import Account, Avatar, Professor, AccountVerifyToken
from serializers import AccountSerializer, BasicAccountSerializer, AuthAccountSerializer, AvatarSerializer, \
	ProfessorSerializer

from script import group, complement
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


def send_verifying_email(account, subject, to, template):
	token_queryset = AccountVerifyToken.objects.all()
	verify_token = uuid.uuid4()
	token_instance, created = AccountVerifyToken.objects.get_or_create(account=account)
	if created or token_instance.is_expired:
		token_instance.expire_time = timezone.now() + timedelta(hours=5)
		token_instance.token = verify_token
		token_instance.save()
	else:
		verify_token = token_instance.token

	print account.first_name
	ctx = {
		'user' : account,
		'token': verify_token,
	}
	email = EmailMessage(subject, render_to_string('email/%s.html' % template, ctx), 'no-reply@classgotcha.com', [to])
	email.content_subtype = 'html'
	email.send()


@api_view(['POST'])
@permission_classes((AllowAny,))
def account_register(request):
	if request.data['email'][-4:] != ".edu":
		return Response(status=status.HTTP_403_FORBIDDEN)

	serializer = AuthAccountSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = serializer.save()
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)

	# TODO: email templates
	send_verifying_email(account=user, subject='[ClassGotcha] Verification Email', to=request.data['email'], template='verification')

	return Response({'token': token}, status=status.HTTP_201_CREATED)


@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def email_verify(request, token=None):
	if request.method == 'GET':
		if request.user.is_verified:
			return Response({'message': 'This email has been verified'}, status=status.HTTP_400_BAD_REQUEST)
		send_verifying_email(account=request.user, subject='[ClassGotcha] Verification Email (resend)', to=request.data['email'], template='verification')
		return Response({'message': 'The verification email has been resent. '}, status=status.HTTP_201_CREATED)
	elif request.method == 'POST':
		if not token:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		token_queryset = AccountVerifyToken.objects.all()
		token_instance = get_object_or_404(token_queryset, token=token)
		# check is_expired
		if token_instance.is_expired:
			return Response({'message': 'Token is expired'}, status=status.HTTP_400_BAD_REQUEST)

		token_instance.account.is_verified = True
		token_instance.is_expired = True
		print token_instance.account, 'has been verified'
		return Response(status=status.HTTP_200_OK)


@api_view(['POST', 'GET', 'PUT'])
@permission_classes((AllowAny,))
def forget_password(request, token=None):
	token_queryset = AccountVerifyToken.objects.all()

	if request.method == 'POST':
		if request.data['email']:
			account = get_object_or_404(Account.objects.all(), email=request.data['email'])
		# USERNAME is not allowed now
		# elif request.data['username']:
		# 	account = get_object_or_404(Account.objects.all(), username=request.data['username'])
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		print account

		reset_token = uuid.uuid4()
		token_instance, created = AccountVerifyToken.objects.get_or_create(account=account)
		if created or token_instance.is_expired:
			token_instance.expire_time = timezone.now() + timedelta(hours=5)
			token_instance.token = reset_token
			token_instance.save()
		else:
			reset_token = token_instance.token

		send_verifying_email(account=account, subject='[ClassGotcha] Reset Password', to=request.data['email'], template='reset')
		return Response({'message': 'The reset password email has been sent. '}, status=status.HTTP_200_OK)

	# verify token
	elif request.method == 'GET':
		# if token not exist return 404 here
		token_instance = get_object_or_404(token_queryset, token=token)
		# check is_expired
		if token_instance.is_expired:
			return Response(status=status.HTTP_404_NOT_FOUND)
		# else return 200
		return Response(status=status.HTTP_200_OK)

	# change password
	elif request.method == 'PUT':
		# if token not exist return 404 here
		token_instance = get_object_or_404(token_queryset, token=token)
		# check is_expired
		if token_instance.is_expired:
			return Response(status=status.HTTP_404_NOT_FOUND)
		# set new password to user
		token_instance.account.set_password(request.data['password'])
		token_instance.account.save()
		token_instance.is_expired = True
		return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'OPTION'])
@permission_classes((IsAuthenticated,))
@parser_classes((MultiPartParser, FormParser,))
def account_avatar(request):
	if request.method == 'POST':
		from StringIO import StringIO
		from django.core.files.uploadedfile import InMemoryUploadedFile
		from resizeimage import resizeimage
		from PIL import Image
		upload = request.FILES.get('file', False)
		if not upload:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		filename, file_extension = upload.name.split('.')
		with Image.open(upload) as image:
			image2x = resizeimage.resize_cover(image, [128, 128])
			image1x = resizeimage.resize_cover(image, [48, 48])
			img2x_name = str(request.user.id) + '.2x' + file_extension
			img1x_name = str(request.user.id) + '.1x' + file_extension
			img2x_io = StringIO()
			img1x_io = StringIO()
			image2x.save(img2x_io, image.format)
			image1x.save(img1x_io, image.format)
			image2x_file = InMemoryUploadedFile(img2x_io, None, img2x_name, 'image/' + image.format,
			                                    img2x_io.len, None)
			image1x_file = InMemoryUploadedFile(img1x_io, None, img1x_name, 'image/' + image.format,
			                                    img1x_io.len, None)

		new_avatar = Avatar.objects.create(avatar2x=image2x_file, avatar1x=image1x_file)
		request.user.avatar = new_avatar
		request.user.save()
		return Response({'data': 'success'}, status=status.HTTP_200_OK)
	elif request.method == 'GET':
		serializer = AvatarSerializer(request.user.avatar)
		return Response(serializer.data)


class AccountViewSet(viewsets.ViewSet):
	queryset = Account.objects.exclude(is_staff=1)
	parser_classes = (MultiPartParser, FormParser, JSONParser)
	permission_classes = (IsAuthenticated,)

	def retrieve(self, request, pk):
		user = get_object_or_404(self.queryset, pk=pk)
		serializer = AccountSerializer(user)
		return Response(serializer.data)

	def destroy(self, request, pk=None):
		if request.user.is_admin or request.user.pk == int(pk):
			user = get_object_or_404(self.queryset, pk=pk)
			user.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)

	def friends(self, request, pk=None):
		if request.method == 'GET':
			serializer = BasicAccountSerializer(request.user.friends, many=True)
			return Response(serializer.data)
		# send friend request
		if request.method == 'POST':
			if request.user.pk is int(pk):  # cant add yourself as your friend
				return Response({'detail': 'cant add yourself as your friend'}, status=status.HTTP_403_FORBIDDEN)
			else:
				new_friend = get_object_or_404(self.queryset, pk=pk)
				if new_friend in request.user.friends.all():
					return Response({'detail': 'Already friended'}, status=status.HTTP_403_FORBIDDEN)

				if request.user in new_friend.pending_friends.all():
					return Response({'detail': 'Already sent the request'}, status=status.HTTP_403_FORBIDDEN)

				new_friend.pending_friends.add(request.user)
				return Response(status=200)

		# accept friend request
		if request.method == 'PUT':
			if request.user.pk is int(pk):  # cant add yourself as your friend
				return Response({'detail': 'cant add yourself as your friend'}, status=status.HTTP_403_FORBIDDEN)
			else:
				new_friend = get_object_or_404(self.queryset, pk=pk)
				if new_friend not in request.user.pending_friends.all():
					return Response({'detail': 'No friend request found'}, status=status.HTTP_403_FORBIDDEN)

				request.user.friends.add(new_friend)
				request.user.pending_friends.remove(new_friend)
				new_friend.friends.add(request.user)
				return Response(status=200)

		if request.method == 'DELETE':
			nomore_friend = get_object_or_404(self.queryset, pk=pk)
			# remove from user friend list
			request.user.friends.remove(nomore_friend)
			request.user.save()
			# if in pending friend list, remove from user pending friend list
			request.user.pending_friends.remove(nomore_friend)
			nomore_friend.friends.remove(request.user)
			nomore_friend.save()
			return Response(status=200)

	@staticmethod
	def me(request):
		if request.method == 'GET':
			serializer = AccountSerializer(request.user)
			return Response(serializer.data)
		elif request.method == 'PUT':
			for (key, value) in request.data.items():
				if key in ['username', 'first_name', 'mid_name', 'last_name', 'gender', 'birthday', 'school_year',
				           'major']:
					if key == 'major':
						request.user.major_id = value
					else:
						setattr(request.user, key, value)
				request.user.save()
			return Response(status=status.HTTP_200_OK)

	@staticmethod
	def change_password(request):
		# If password or old-password not in request body
		if not request.data['old-password'] or request.data['password']:
			# Return error message with status code 400
			return Response(status=status.HTTP_400_BAD_REQUEST)
		try:
			#  if old-password match
			if check_password(request.data['old-password'], request.user.password):
				# change user password
				request.user.set_password(request.data['password'])
				request.user.save()
				return Response(status=status.HTTP_200_OK)
			else:
				# else return with error message and status code 400
				return Response({'ERROR': 'Password not match'}, status=status.HTTP_400_BAD_REQUEST)
		except:
			# If exception return with status 400
			return Response(status=status.HTTP_400_BAD_REQUEST)

	@staticmethod
	def pending_friends(request):
		serializer = BasicAccountSerializer(request.user.pending_friends, many=True)
		return Response(serializer.data)

	@staticmethod
	def classrooms(request, pk=None):
		classroom_queryset = Classroom.objects.all()

		if request.method == 'GET':
			classrooms = Classroom.objects.filter(students__pk=request.user.pk).order_by('major')
			serializer = BasicClassroomSerializer(classrooms, many=True)
			return Response(serializer.data)

		if request.method == 'POST':
			classroom = get_object_or_404(classroom_queryset, pk=pk)
			# add user to classroom student list
			classroom.students.add(request.user)
			# add class time to user task list
			classroom.class_time.involved.add(request.user)
			# add classroom tasks from user task list
			for task in classroom.tasks.all():
				task.involved.add(request.user)
			# add user to classroom chatrooms
			# TODO: change into matrix version: classroom.chatrooms.get().accounts.add(request.user.username ???)
			# also need to call the matrix api? add the user into matrix chatrooms...
			classroom.chatroom.get().accounts.add(request.user)
			return Response(status=200)

		if request.method == 'DELETE':
			classroom = get_object_or_404(classroom_queryset, pk=pk)
			# remove user from classroom student list
			classroom.students.remove(request.user)
			# remove classroom time form user task list
			classroom.class_time.involved.remove(request.user)
			# remove classroom tasks from user task list
			for task in classroom.tasks.all():
				task.involved.remove(request.user)
			# remove user from classroom chatrooms
			classroom.chatroom.get().accounts.remove(request.user)
			return Response(status=200)

	@staticmethod
	def notes(request):
		serializer = NoteSerializer(request.user.notes.all(), many=True)
		return Response(serializer.data)

	@staticmethod
	def moments(request, pk=None):
		moment_query_set = request.user.moments.filter(deleted=False).order_by('-created')
		# Only return first 20 moments
		if request.method == 'GET':
			serializer = MomentSerializer(moment_query_set[0:20], many=True)
			return Response(serializer.data)
		elif request.method == 'POST':
			content = request.data.get('content', None)
			classroom_id = request.data.get('classroom_id', None)
			question = request.data.get('question', None)
			image = request.data.get('file', None)
			# Data missing, return 400
			if not content and not question:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			# create new moment
			moment = Moment(content=content, creator=request.user)
			if classroom_id:
				moment.classroom_id = classroom_id
			if question:
				moment.solved = False
			if image:
				import uuid
				from django.core.files.base import ContentFile
				from base64 import b64decode
				header, image = image.split(';base64,')
				file_extension = header.split('/')[1]
				try:
					decoded_file = b64decode(image)
				except TypeError:
					return Response({'detail': 'invalid image!'}, status=status.HTTP_400_BAD_REQUEST)
				file_name = str(uuid.uuid4())
				complete_file_name = '%s.%s' % (file_name, file_extension,)
				moment.images = ContentFile(decoded_file, complete_file_name)
			moment.save()
			return Response(status=status.HTTP_200_OK)
		elif request.method == 'PUT':
			moment = get_object_or_404(moment_query_set, pk=pk)
			if moment.solved is False:
				moment.solved = True
				moment.save()
			return Response(status=status.HTTP_200_OK)
		elif request.method == 'DELETE':
			moment = get_object_or_404(moment_query_set, pk=pk)
			moment.deleted = True
			moment.save()
			return Response(status=status.HTTP_200_OK)

	@staticmethod
	def rooms(request, pk=None):
		room_query_set = request.user.rooms.all()
		if request.method == 'GET':
			serializer = ChatroomSerializer(room_query_set, many=True)
			return Response(serializer.data)
		elif request.method == 'POST':
			room = get_object_or_404(room_query_set, pk)
			room.accounts.add(request.user)
			room.save()
			return Response(status=status.HTTP_200_OK)
		elif request.method == 'DELETE':
			room = get_object_or_404(room_query_set, pk)
			room.accounts.delete(request.user)
			room.save()
			return Response(status=status.HTTP_200_OK)

	@staticmethod
	def tasks(request, pk=None):
		task_queryset = request.user.tasks.all()
		if request.method == 'GET':
			serializer = TaskSerializer(task_queryset, many=True)
			return Response(serializer.data)
		elif request.method == 'POST':
			serializer = TaskSerializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)
		elif request.method == 'PUT':
			task = get_object_or_404(task_queryset, pk=pk)
			task.involved.remove(request.user)
			task.finished.add(request.user)
			return Response(status=status.HTTP_200_OK)
		elif request.method == 'DELETE':
			task = get_object_or_404(task_queryset, pk=pk)
			task.involved.remove(request.user)
			if task.involved.length == 0:
				task.delete()
			return Response(status=status.HTTP_200_OK)

	@staticmethod
	def free_time(request):
		user_tasks = request.user.tasks.all()
		# loop through the tasks
		free_time_dict = {'Mon': [], 'Tue': [], 'Wed': [], 'Thu': [], 'Fri': [], 'Sat': [], 'Sun': []}
		for task in user_tasks:
			try:
				start_time = task.start.hour + task.start.minute * (1 / 60)
				end_time = task.end.hour + task.end.minute * (1 / 60)
			except:
				pass
			if 'Mo' in task.repeat:
				free_time_dict['Mon'].append([start_time, end_time])

			if 'Tu' in task.repeat:
				free_time_dict['Tue'].append([start_time, end_time])

			if 'We' in task.repeat:
				free_time_dict['Wed'].append([start_time, end_time])

			if 'Th' in task.repeat:
				free_time_dict['Thu'].append([start_time, end_time])

			if 'Fr' in task.repeat:
				free_time_dict['Fri'].append([start_time, end_time])

		# compute the intersections and return
		print free_time_dict
		for free_dict_list in free_time_dict:
			intervals = free_time_dict[free_dict_list]
			free_dict_list = group(intervals)  # find the union of all unavailable time
			print intervals
			free_dict_list = complement(intervals, first=0, last=24)

		return Response({'freetime': free_time_dict}, status=status.HTTP_200_OK)

	@staticmethod
	def home_page_activity(request):
		# TODO: show latest activity related to me
		# include moments, comments, notes my classmates and friends posted
		classrooms = Classroom.objects.filter(students__pk=request.user.pk)

		moments = Moment.objects.filter(classroom__in=classrooms).filter(deleted=False).order_by('-created')[0:20]
		serializer = MomentSerializer(moments, many=True)
		return Response(serializer.data)


class ProfessorViewSet(viewsets.ViewSet):
	queryset = Professor.objects.all()
	parser_classes = (MultiPartParser, FormParser, JSONParser)
	permission_classes = (IsAuthenticated,)

	def retrieve(self, request, pk):
		professor = get_object_or_404(self.queryset, pk=pk)
		serializer = ProfessorSerializer(professor)
		return Response(serializer.data)

	def update(self, request, pk):
		professor = get_object_or_404(self.queryset, pk=pk)
		for (key, value) in request.data.items():
			if key in ['first_name', 'last_name', 'email', 'office', 'major']:
				if key is 'major':
					setattr(professor, 'major_id', value)
				else:
					setattr(professor, key, value)
		return Response(status=status.HTTP_200_OK)

	def comments(self, request, pk):
		if request.method == 'GET':
			professor = get_object_or_404(self.queryset, pk=pk)
			comments = professor.comments.all()
			return Response(CommentSerializer(comments, many=True).data)
		elif request.method == 'POST':
			content = request.data.get('content')
			num = request.data.get('num')
			if content and num:
				professor = get_object_or_404(self.queryset, pk=pk)
				comment = Comment.objects.create(content=content)
				rate = Rate.objects.create(num=num)
				rate.professor = professor
				rate.creator = request.user
				rate.save()
				comment.professor = professor
				comment.creator = request.user
				comment.rate = rate
				comment.save()
				return Response(status=status.HTTP_201_CREATED)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)

	def classrooms(self, request, pk):
		pass


class GroupViewSet(viewsets.ViewSet):
	pass
