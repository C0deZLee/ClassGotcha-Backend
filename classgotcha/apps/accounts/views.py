from  datetime import datetime

from django.shortcuts import get_object_or_404
from django.core.files.base import File

from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from serializers import AccountSerializer, BasicAccountSerializer, AuthAccountSerializer, AvatarSerializer
from ..classrooms.serializers import Classroom, BasicClassroomSerializer
from ..posts.serializers import Moment, MomentSerializer, NoteSerializer
from ..chat.serializers import RoomSerializer, Room
from ..tasks.serializers import TaskSerializer

from models import Account, Avatar

from script import group, complement


@api_view(['POST'])
@permission_classes((AllowAny,))
def account_register(request):
	serializer = AuthAccountSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = serializer.save()
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)
	return Response({'token': token}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'OPTION'])
@permission_classes((IsAuthenticated,))
@parser_classes((MultiPartParser, FormParser,))
def account_avatar(request):
	import os
	from resizeimage import resizeimage
	from PIL import Image

	if request.method == 'POST':
		upload = request.FILES.get('file', False)
		if not upload:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		filename, file_extension = os.path.splitext(upload.name)

		with open(filename, 'wb+') as avatar:
			for chunk in upload.chunks():
				avatar.write(chunk)
			with Image.open(avatar) as image:
				image4x = resizeimage.resize_cover(image, [512, 512])
				image2x = resizeimage.resize_cover(image, [128, 128])
				image1x = resizeimage.resize_cover(image, [48, 48])
				img4x_name = str(request.user.id) + '.4x' + file_extension
				img2x_name = str(request.user.id) + '.2x' + file_extension
				img1x_name = str(request.user.id) + '.1x' + file_extension
				image4x.save(img4x_name, image.format)
				image2x.save(img2x_name, image.format)
				image1x.save(img1x_name, image.format)

		img4x = open(img4x_name)
		img2x = open(img2x_name)
		img1x = open(img1x_name)

		new_avatar = Avatar(avatar4x=File(file=img4x), avatar2x=File(file=img2x), avatar1x=File(file=img1x))
		new_avatar.save()
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

	# list_route and detail_route are for auto gen URL
	@staticmethod
	def me(request):
		serializer = AccountSerializer(request.user)
		return Response(serializer.data)

	def retrieve(self, request, pk):
		user = get_object_or_404(self.queryset, pk=pk)
		serializer = AccountSerializer(user)
		return Response(serializer.data)

	def update(self, request, pk):
		if request.user.is_admin or request.user.id == int(pk):
			user = get_object_or_404(self.queryset, pk=pk)
			# apply every key, value pair to this user instance
			for (key, value) in request.data.items():
				if key in ['username', 'first_name', 'mid_name', 'last_name', 'gender', 'birthday', 'school_year',
				           'major']:
					setattr(user, key, value)
			user.save()
			serializer = AccountSerializer(user)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)

	def destroy(self, request, pk=None):
		if request.user.is_admin or request.user.pk == int(pk):
			user = get_object_or_404(self.queryset, pk=pk)
			user.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)

	# verify past password
	@staticmethod
	def reset_password(self, request, pk=None):
		if request.user.is_admin or request.user.pk == int(pk):
			if not request.data['old-password']:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			try:
				request.user.set_password(request.data['password'])
				request.user.save()
				return Response(status=200)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)

	def friends(self, request, pk=None):
		if request.method == 'GET':
			serializer = BasicAccountSerializer(request.user.friends, many=True)
			return Response(serializer.data)

		if request.method == 'POST':
			if request.user.pk is int(pk):  # cant add yourself as your friend
				return Response({'detail': 'cant add yourself as your friend'}, status=status.HTTP_403_FORBIDDEN)
			else:
				new_friend = get_object_or_404(self.queryset, pk=pk)
				if new_friend in request.user.friends.all():
					return Response({'detail': 'friend already in list'}, status=status.HTTP_403_FORBIDDEN)
				request.user.friends.add(new_friend)
				request.user.save()
				new_friend.friends.add(request.user)
				new_friend.save()

				return Response(status=200)

		if request.method == 'DELETE':
			was_friend = get_object_or_404(self.queryset, pk=pk)
			request.user.friends.remove(was_friend)
			request.user.save()
			was_friend.friends.remove(request.user)
			was_friend.save()
			return Response(status=200)

	@staticmethod
	def classrooms(request, pk=None):
		classroom_queryset = Classroom.objects.all()
		chatroom_queryset = Room.objects.all()

		if request.method == 'GET':
			classrooms = Classroom.objects.filter(students__pk=request.user.pk)
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
			# add user to classroom chatroom
			chatroom = get_object_or_404(chatroom_queryset, classroom_id=classroom.pk)
			chatroom.accounts.add(request.user)
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
			# remove user from classroom chatroom
			chatroom = get_object_or_404(chatroom_queryset, classroom_id=classroom.pk)
			chatroom.accounts.remove(request.user)
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

		if request.method == 'POST':
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
				complete_file_name = "%s.%s" % (file_name, file_extension,)
				moment.images = ContentFile(decoded_file, complete_file_name)
			moment.save()
			return Response(status=status.HTTP_200_OK)

		if request.method == 'PUT':
			moment = get_object_or_404(moment_query_set, pk=pk)
			if moment.solved is False:
				moment.solved = True
				moment.save()
			return Response(status=status.HTTP_200_OK)
		if request.method == 'DELETE':
			moment = get_object_or_404(moment_query_set, pk=pk)
			moment.deleted = True
			moment.save()
			return Response(status=status.HTTP_200_OK)

	@staticmethod
	def rooms(request, pk=None):
		room_query_set = request.user.rooms.all()
		if request.method == 'GET':
			serializer = RoomSerializer(room_query_set, many=True)
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

	# def recent_activity(self, request):
	# 	# TODO: show recent activity in profile page
	# 	# include posted moments, comments, notes
	# 	pass

	def home_page_activity(self, request):
		# TODO: show latest activity related to me
		# include moments, comments, notes my classmates and friends posted
		classrooms = Classroom.objects.filter(students__pk=request.user.pk)

		moments = Moment.objects.filter(classroom__in=classrooms).filter(deleted=False).order_by('-created')[0:20]
		serializer = MomentSerializer(moments, many=True)
		return Response(serializer.data)


class GroupViewSet(viewsets.ViewSet):
	pass
