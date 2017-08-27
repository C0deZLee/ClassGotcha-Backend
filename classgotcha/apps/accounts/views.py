import uuid
from django.utils import timezone
from datetime import timedelta

from django.shortcuts import get_object_or_404
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

from ..notifications.models import Notification

from models import Account, Professor, AccountVerifyToken
from serializers import AccountSerializer, BasicAccountSerializer, AuthAccountSerializer, ProfessorSerializer

from script import group, complement, generate_recommendations_for_homework
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from ..badges.script import trigger_action


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

	ctx = {
		'user' : account,
		'token': verify_token,
	}
	email = EmailMessage(subject, render_to_string('email/%s.html' % template, ctx), 'no-reply@classgotcha.com', [to])
	email.content_subtype = 'html'
	email.send()


# For Friend Searching
def is_similar(user1, user2):
	return (lambda a, b, c: len(a) / float(len(b)) > .8 and len(a) / float(len(c)) > .8 if b and c else False)(user1.classroom.intersects(user2.classroom), user1.classroom, user2.classroom)


@api_view(['POST'])
@permission_classes((AllowAny,))
def account_register(request):
	if request.data['email'][-4:] != ".edu":
		return Response({'email': ['Please use your edu email.']}, status=status.HTTP_403_FORBIDDEN)
	if request.data.get('refer'):
		referrer = Account.objects.get(email=request.data.get('refer'))
		trigger_action(referrer, 'refer_friend')

	serializer = AuthAccountSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = serializer.save()
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)

	referrer = request.data.get('referrer', None)
	if referrer:
		account = Account.objects.get(email=referrer)
		if account:
			trigger_action(account, 'refer_friend')
			Notification.objects.create(sender_id=user.id, content='joined ClassGotcha with your refer!', receiver_id=account.id)

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
		trigger_action(request.user, 'verify_email')

		return Response(status=status.HTTP_200_OK)


@api_view(['POST', 'GET', 'PUT'])
@permission_classes((AllowAny,))
def forget_password(request, token=None):
	token_queryset = AccountVerifyToken.objects.all()

	if request.method == 'POST':
		if request.data['email']:
			account = get_object_or_404(Account.objects.all(), email=request.data['email'])
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

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


@api_view(['POST', 'OPTIONS'])
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
			image2x = resizeimage.resize_cover(image, [100, 100])
			image1x = resizeimage.resize_cover(image, [50, 50])
			img2x_name = str(request.user.id) + '.100.' + file_extension
			img1x_name = str(request.user.id) + '.50.' + file_extension
			img2x_io = StringIO()
			img1x_io = StringIO()
			image2x.save(img2x_io, image.format)
			image1x.save(img1x_io, image.format)
			image2x_file = InMemoryUploadedFile(img2x_io, None, img2x_name, 'image/' + image.format,
			                                    img2x_io.len, None)
			image1x_file = InMemoryUploadedFile(img1x_io, None, img1x_name, 'image/' + image.format,
			                                    img1x_io.len, None)
		request.user.avatar1x = image1x_file
		request.user.avatar2x = image2x_file

		request.user.save()
		trigger_action(request.user, 'change_avatar')
		return Response({'data': 'success'}, status=status.HTTP_200_OK)


class AccountViewSet(viewsets.ViewSet):
	queryset = Account.objects.all()
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

	def search(self, request):
		token = request.data.get('token', None)
		if token:
			# TODO: search implementation
			# Assume token is "abcd1234@psu.edu" or "abcd1234" or "John Martin"
			# ....
			# ....
			users = []
			serializer = BasicAccountSerializer(users, many=True)

			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def friends(self, request, pk=None):
		if request.method == 'GET':
			serializer = BasicAccountSerializer(request.user.friends, many=True)
			return Response(serializer.data)
		# send friend request
		if request.method == 'POST':
			if request.user.pk is int(pk):  # cant add yourself as your friend
				return Response({'detail': 'You can\'t add yourself as friend'}, status=status.HTTP_403_FORBIDDEN)
			else:
				new_friend = get_object_or_404(self.queryset, pk=pk)
				if new_friend in request.user.friends.all():
					return Response({'detail': 'Already friend'}, status=status.HTTP_403_FORBIDDEN)

				if request.user in new_friend.pending_friends.all():
					return Response({'detail': 'You have sent friend request, please wait response'}, status=status.HTTP_403_FORBIDDEN)

				new_friend.pending_friends.add(request.user)

				trigger_action(request.user, 'add_friend')
				return Response(status=200)

		# accept friend request
		if request.method == 'PUT':
			if request.user.pk is int(pk):  # cant add yourself as your friend
				return Response({'detail': 'You can\'t add yourself as your friend'}, status=status.HTTP_403_FORBIDDEN)
			else:
				new_friend = get_object_or_404(self.queryset, pk=pk)
				if new_friend not in request.user.pending_friends.all():
					return Response({'detail': 'No friend request found'}, status=status.HTTP_403_FORBIDDEN)

				request.user.friends.add(new_friend)
				request.user.pending_friends.remove(new_friend)
				new_friend.friends.add(request.user)

				trigger_action(request.user, 'accept_friend')
				trigger_action(new_friend, 'accept_friend')

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
				if key == 'major':
					request.user.major_id = value

				if key in ['username', 'first_name', 'last_name', 'gender', 'birthday', 'school_year', 'about_me', 'phone', 'privacy_setting', 'facebook', 'twitter', 'linkedin', 'snapchat']:
					setattr(request.user, key, value)
				request.user.save()
			return Response(status=status.HTTP_200_OK)

	@staticmethod
	def change_password(request):
		print request.data

		# If password or old-password not in request body
		if not (request.data.get('old_password', None) or request.data.get('new_password', None)):
			# Return error message with status code 400
			return Response(status=status.HTTP_400_BAD_REQUEST)
		# try:
		#  if old-password match
		if check_password(request.data['old_password'], request.user.password):
			# change user password
			request.user.set_password(request.data['new_password'])
			request.user.save()
			return Response(status=status.HTTP_200_OK)
		else:
			# else return with error message and status code 400
			return Response({'detail': 'Doesn\'t match with your current password.'}, status=status.HTTP_400_BAD_REQUEST)
		# except:
		# 	# If exception return with status 400
		# 	return Response(status=status.HTTP_400_BAD_REQUEST)

	def explore_friends(self, request):
		def similarity_check_classrooms(user, other):
			# return boolean whether they could be friends [based on the classroom list]
			# if other.classrooms.all():
			# 	print "this is not empty\n"
			mine = set(user.classrooms.all())
			his = set(other.classrooms.all())
			return True if mine and his and (mine <= his or mine > his or len(mine & his) >= 2) else False

		# def sharing_friends(user, other):
		# 	# return boolean

		possible_friends = []
		# Explore Friends basing on classrooms
		for account in self.queryset:
			if account not in (request.user.friends.all() | request.user.pending_friends.all()) and similarity_check_classrooms(request.user, account):
				possible_friends.append(account)
		serializer = BasicAccountSerializer(possible_friends, many=True)
		return Response(serializer.data)

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

			trigger_action(request.user, 'add_classroom')

			# add user to classroom chatrooms
			# change into matrix version: classroom.chatrooms.get().accounts.add(request.user.username ???)
			# also need to call the matrix api? add the user into matrix chatrooms...
			# classroom.chatroom.get().accounts.add(request.user)
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
			# classroom.chatroom.get().accounts.remove(request.user)
			return Response(status=200)

	@staticmethod
	def notes(request):
		serializer = NoteSerializer(request.user.notes.all(), many=True)
		return Response(serializer.data)

	@staticmethod
	def moments(request, pk=None):
		if not pk:
			moment_query_set = request.user.moments.filter(deleted=False).order_by('-created')
		else:
			moment_query_set = Account.objects.get(pk=pk).moments.filter(deleted=False).order_by('-created')

		if request.method == 'GET':
			# Only return first 20 moments
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
				trigger_action(request.user, 'post_question')
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
			trigger_action(request.user, 'post_moment')
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

	@staticmethod
	def study_plan(request):
		user_tasks = request.user.tasks.all()
		user = request.user
		for task in user_tasks:
			# generate_recommendations_for_homework(user, task)
			pass
		# TODO: study plan generator, all generated plan should be category 6
		# ....
		return Response(status=status.HTTP_200_OK)


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
		professor = get_object_or_404(self.queryset, pk=pk)
		if request.method == 'GET':
			comments = professor.comments.all()
			return Response(CommentSerializer(comments, many=True).data)
		elif request.method == 'POST':
			content = request.data.get('content', '')
			is_anonymous = request.data.get('is_anonymous')
			# num = request.data.get('num')
			if content:
				comment = Comment.objects.create(content=content,
				                                 professor_id=professor.id,
				                                 is_anonymous=is_anonymous,
				                                 creator=request.user)
				comment.save()
				return Response(status=status.HTTP_201_CREATED)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)

	def classrooms(self, request, pk):
		pass
