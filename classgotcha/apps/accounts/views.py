from django.conf import settings
from models import Account, Avatar
from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from serializers import AccountSerializer, AuthAccountSerializer, AvatarSerializer

from permissions import IsAdminOrSelf

from boto.s3.connection import S3Connection
from boto.s3.key import Key

from ..classrooms.models import Classroom
from ..classrooms.serializers import ClassroomSerializer


class AccountViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	Additionally we also provide an extra `highlight` action.
	"""
	queryset = Account.objects.all()
	permission_classes = (IsAuthenticatedOrReadOnly,)
	serializer_class = AccountSerializer
	parser_classes = (FormParser, MultiPartParser,)
	# pagination_class =

	@detail_route(
		methods=['put', 'get', 'delete'],
		permission_classes=(IsAuthenticated,),
	)
	def friends(self, request, pk=None):
		if request.method == 'GET':
			friends = request.user.friends
			serializer = AccountSerializer(friends, many=True)
			return Response(serializer.data)
		elif request.method == 'PUT':
			new_friend = Account.objects.get(pk=pk)
			if not new_friend:
				return Response(status=404)
			else:
				request.user.friends.add(new_friend)
				request.user.save()
				return Response(status=200)
		else:
			was_friend = Account.objects.get(pk=pk)
			if not was_friend:
				return Response(status=404)
			else:
				request.user.friends.remove(was_friend)
				request.user.save()
				return Response(status=200)

	@detail_route(
		methods=['put', 'get', 'delete'],
		permission_classes=(IsAuthenticated,),
		serializer_class=ClassroomSerializer
	)
	def classrooms(self, request, pk=None):
		if request.method == 'GET':
			classrooms = Classroom.objects.filter(students__pk=request.user.pk)
			serializer = ClassroomSerializer(classrooms, many=True)
			return Response(serializer.data)
		elif request.method == 'PUT':
			classroom = Classroom.objects.get(pk=pk)
			if not classroom:
				return Response(status=404)
			else:
				classroom.students.add(request.user)
				classroom.save()
				return Response(status=200)
		else:
			classroom = Classroom.objects.get(pk=pk)
			if not classroom:
				return Response(status=404)
			else:
				# TODO: test if user is in classroom
				classroom.students.remove(request.user)
				classroom.save()
				return Response(status=200)

	@detail_route(
		methods=['post', 'put', 'get'],
		permission_classes=(IsAuthenticatedOrReadOnly,),
		serializer_class=AvatarSerializer,
		parser_classes=(FormParser, MultiPartParser,)
	)
	def avatar(self, request, pk=None):
		if request.method in ['POST', 'OPTION']:
			upload = request.FILES['avatar']
			if not upload:
				return Response(status=400)

			filename = 'myfile'
			with open(filename, 'wb+') as temp_file:
				for chunk in upload.chunks():
					temp_file.write(chunk)
			avatar = open(filename)  # there you go
			new_avatar = Avatar(full_image=avatar)
			new_avatar.save()
			return Response(status=200)
		else:
			avatar = request.user.avatar
			serializer = AvatarSerializer(avatar)
			return Response(serializer.data)


class AccountMe(generics.GenericAPIView):
	serializer_class = AccountSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Account.objects.filter(pk=self.request.user.pk)


# class AvatarUpload(viewsets.ModelViewSet):
# 	queryset = Account.objects.all()
# 	parser_classes = (MultiPartParser, FormParser)
# 	serializer_class = AvatarSerializer
#
# 	def upload_avatar(self, request, format=None):
# 		upload = request.FILES['avatar']
# 		if not upload:
# 			return Response(status=404)
#
# 		filename = 'myfile'
# 		with open(filename, 'wb+') as temp_file:
# 			for chunk in upload.chunks():
# 				temp_file.write(chunk)
# 		avatar = open(filename)  # there you go
# 		new_avatar = Avatar(full_image=avatar)
# 		new_avatar.save()
# 		return Response(status=200)
#
# #
# 	file_obj = request.FILES['file']
#
# 	upload = Account(user=request.user, avatar=file_obj.seek(0))
# 	upload.save()
#
# 	conn = S3Connection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
# 	k = Key(conn.get_bucket(settings.AWS_S3_BUCKET))
# 	k.key = 'upls/%s/%s.png' % (request.user.id, upload.key)
# 	k.set_contents_from_string(file_obj.read())
#
# 	serializer = UploadSerializer(upload)
#
# 	return Response(serializer.data, status=201)

# from rest_framework.decorators import detail_route
#
# class AccountViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#
#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#
#     @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
#     def highlight(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
