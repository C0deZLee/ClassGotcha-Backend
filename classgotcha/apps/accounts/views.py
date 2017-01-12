import os
from models import Account, Avatar
from django.shortcuts import get_object_or_404
from django.core.files.base import File
from rest_framework_jwt.settings import api_settings
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.decorators import detail_route, list_route, api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

from serializers import AccountSerializer, AvatarSerializer

from ..classrooms.models import Classroom
from ..classrooms.serializers import ClassroomSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def account_register(request):
	serializer = AccountSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = serializer.save()
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)
	return Response({'token': token}, status=status.HTTP_201_CREATED)


@api_view(['POST', 'OPTION'])
@permission_classes((IsAuthenticated,))
@parser_classes((MultiPartParser, FormParser,))
def account_avatar(request):
	try:
		upload = request.FILES['file']
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)
	filename, file_extension = os.path.splitext(upload.name)
	filename = str(request.user.id) + file_extension
	with open(filename, 'wb+') as temp_file:
		for chunk in upload.chunks():
			temp_file.write(chunk)
	avatar = open(filename)  # there you go
	new_file = File(file=avatar)
	new_avatar = Avatar(full_image=new_file)
	new_avatar.save()
	request.user.avatar = new_avatar
	request.user.save()
	return Response(status=status.HTTP_200_OK)


class AccountViewSet(viewsets.ViewSet):
	queryset = Account.objects.exclude(is_staff=1)
	parser_classes = (FormParser, MultiPartParser,)
	permission_classes = (IsAuthenticated,)
	# list_route and detail_route are for auto gen URL

	def list(self, request):
		serializer = AccountSerializer(self.queryset, many=True)
		return Response(serializer.data)

	def me(self, request):
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
				if key in ['username', 'first_name', 'mid_name', 'last_name', 'gender', 'birthday', 'school_year', 'major']:
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

	def reset_password(self, request, pk=None):
		if request.user.is_admin or request.user.pk == int(pk):
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
			serializer = AccountSerializer(request.user.friends, many=True)
			return Response(serializer.data)

		if request.method == 'POST':
			if request.user.pk is int(pk): # cant add yourself as your friend
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

	def classrooms(self, request, pk=None):
		classroom_queryset = Classroom.objects.all()
		if request.method == 'GET':
			classrooms = Classroom.objects.filter(students__pk=request.user.pk)
			serializer = ClassroomSerializer(classrooms, many=True)
			return Response(serializer.data)

		if request.method == 'POST':
			classroom = get_object_or_404(classroom_queryset, pk=pk)
			if request.user in classroom.students.all():
				return Response({'detail': 'student already in classroom'}, status=status.HTTP_403_FORBIDDEN)
			classroom.students.add(request.user)
			classroom.save()
			return Response(status=200)

		if request.method == 'DELETE':
			classroom = get_object_or_404(classroom_queryset, pk=pk)
			# TODO: test if user is in classroom
			classroom.students.remove(request.user)
			classroom.save()
			return Response(status=200)


class AccountMe(generics.GenericAPIView):
	serializer_class = AccountSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Account.objects.filter(pk=self.request.user.pk)
