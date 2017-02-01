import os
from resizeimage import resizeimage
from PIL import Image

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
	if request.method == 'POST':
		try:
			upload = request.FILES['file']
		except:
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
	parser_classes = (FormParser, MultiPartParser, JSONParser)
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

	# TODO: FIXME, 403 forbidden front enf, post man 500
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
			if request.user in classroom.students.all():
				return Response({'detail': 'student already in classroom'}, status=status.HTTP_403_FORBIDDEN)
			classroom.students.add(request.user)
			classroom.class_time.involved.add(request.user)
			chatroom = get_object_or_404(chatroom_queryset, classroom_id=classroom.pk)
			chatroom.accounts.add(request.user)
			return Response(status=200)

		if request.method == 'DELETE':
			classroom = get_object_or_404(classroom_queryset, pk=pk)
			classroom.students.remove(request.user)
			classroom.class_time.involved.remove(request.user)
			classroom.class_room.accounts.remove(request.user)
			classroom.save()
			classroom.class_time.save()
			classroom.chatroom.save()
			return Response(status=200)

	@staticmethod
	def notes(request):
		serializer = NoteSerializer(request.user.notes.all(), many=True)
		return Response(serializer.data)

	@staticmethod
	def moments(request, pk=None):
		moment_query_set = request.user.moments.filter(deleted=False)
		# Only return first 20 moments
		if request.method == 'GET':
			serializer = MomentSerializer(moment_query_set.reverse()[0:20], many=True)
			return Response(serializer.data)

		if request.method == 'POST':
			# TODO: img upload
			content = request.data.get('content', None)
			classroom_id = request.data.get('classroom_id', None)
			question = request.data.get('question', None)

			if not content and not question:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			# create new moment
			moment = Moment(content=content, creator=request.user)
			if classroom_id:
				moment.classroom_id = classroom_id
			if question:
				moment.solved = False
			moment.save()
			return Response(status=status.HTTP_200_OK)

		if request.method == 'DELETE':
			moment = get_object_or_404(moment_query_set, pk)
			moment.deleted = True
			moment.save()
			return Response(status=status.HTTP_200_OK)

	@staticmethod
	def moments_pagination(request, page=None):
		# TODO: can optimize here
		if not page:
			page = 0
		else:
			page = int(page)
		serializer = MomentSerializer(request.user.moments.all().reverse()[page:page + 5], many=True)
		return Response(serializer.data)

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
	def tasks(request):
		serializer = TaskSerializer(request.user.tasks.all(), many=True)
		return Response(serializer.data)

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

	def recent_activity(self, request):
		# TODO: show recent activity in profile page
		# include posted moments, comments, notes
		pass

	def home_page_activity(self, request):
		# TODO: show latest activity related to me
		# include moments, comments, notes my classmates and friends posted
		pass


class GroupViewSet(viewsets.ViewSet):
	pass
