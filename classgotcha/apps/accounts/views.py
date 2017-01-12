from models import Account, Avatar
from django.shortcuts import get_object_or_404
from rest_framework_jwt.settings import api_settings
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import detail_route, list_route, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from permissions import IsAnonymous

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


class AccountViewSet(viewsets.ViewSet):
	queryset = Account.objects.exclude(is_staff=1)
	parser_classes = (FormParser, MultiPartParser,)
	permission_classes = (IsAuthenticated,)
	# lookup_field = 'pk'
	# TODO: list_route and detail_route are not working as expected

	@list_route()
	def list(self, request):
		serializer = AccountSerializer(self.queryset, many=True)
		return Response(serializer.data)

	@detail_route(methods=['get'])
	def me(self, request):
		serializer = AccountSerializer(request.user)
		return Response(serializer.data)

	@detail_route(methods=['get'])
	def retrieve(self, request, pk):
		user = get_object_or_404(self.queryset, pk=pk)
		serializer = AccountSerializer(user)
		return Response(serializer.data)

	@detail_route(methods=['post'])
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

	@detail_route(methods=['delete'])
	def destroy(self, request, pk=None):
		if request.user.is_admin or request.user.pk == int(pk):
			user = get_object_or_404(self.queryset, pk=pk)
			user.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)

	@detail_route(methods=['post'])
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

	@list_route()
	def friend_list(self, request):
		serializer = AccountSerializer(request.user.friends, many=True)
		return Response(serializer.data)

	@detail_route(methods=['post', 'delete'])
	def friends(self, request, pk=None):
		if request.method == 'POST':
			if request.user.pk is not int(pk): # cant add yourself as your friend
				new_friend = get_object_or_404(self.queryset, pk=pk)
				request.user.friends.add(new_friend)
				request.user.save()
				new_friend.friends.add(request.user)
				new_friend.save()
				return Response(status=200)
			else:
				return Response({'error': 'cant add yourself as your friend'}, status=status.HTTP_403_FORBIDDEN)

		if request.method == 'DELETE':
			was_friend = get_object_or_404(self.queryset, pk=pk)
			request.user.friends.remove(was_friend)
			request.user.save()
			was_friend.friends.remove(request.user)
			was_friend.save()
			return Response(status=200)

	@detail_route(methods=['put', 'get', 'delete'], permission_classes=(IsAuthenticated,), serializer_class=ClassroomSerializer)
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
		methods=['post', 'put', 'get', 'option'],
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

#
# class AccountViewSet(viewsets.ModelViewSet):
#
# 	queryset = Account.objects.exclude(is_superuser=1)
# 	# permission_classes = (IsAuthenticatedOrReadOnly,)
# 	serializer_class = AccountSerializer
# 	parser_classes = (FormParser, MultiPartParser,)
# 	lookup_field = 'pk'
#
# 	@detail_route(methods=['post', 'get', 'delete'], permission_classes=(IsAuthenticated,))
# 	def friends(self, request, pk=None):
# 		if request.method == 'GET':
# 			friends = request.user.friends
# 			serializer = AccountSerializer(friends, many=True)
# 			return Response(serializer.data)
# 		elif request.method == 'POST':
# 			new_friend = Account.objects.get(pk=pk)
# 			if not new_friend:
# 				return Response(status=404)
# 			else:
# 				request.user.friends.add(new_friend)
# 				request.user.save()
# 				return Response(status=200)
# 		else:
# 			was_friend = Account.objects.get(pk=pk)
# 			if not was_friend:
# 				return Response(status=404)
# 			else:
# 				request.user.friends.remove(was_friend)
# 				request.user.save()
# 				return Response(status=200)
#
# 	@detail_route(
# 		methods=['put', 'get', 'delete'],
# 		permission_classes=(IsAuthenticated,),
# 		serializer_class=ClassroomSerializer
# 	)
# 	def classrooms(self, request, pk=None):
# 		if request.method == 'GET':
# 			classrooms = Classroom.objects.filter(students__pk=request.user.pk)
# 			serializer = ClassroomSerializer(classrooms, many=True)
# 			return Response(serializer.data)
# 		elif request.method == 'PUT':
# 			classroom = Classroom.objects.get(pk=pk)
# 			if not classroom:
# 				return Response(status=404)
# 			else:
# 				classroom.students.add(request.user)
# 				classroom.save()
# 				return Response(status=200)
# 		else:
# 			classroom = Classroom.objects.get(pk=pk)
# 			if not classroom:
# 				return Response(status=404)
# 			else:
# 				# TODO: test if user is in classroom
# 				classroom.students.remove(request.user)
# 				classroom.save()
# 				return Response(status=200)
#
# 	@detail_route(
# 		methods=['post', 'put', 'get', 'option'],
# 		permission_classes=(IsAuthenticatedOrReadOnly,),
# 		serializer_class=AvatarSerializer,
# 		parser_classes=(FormParser, MultiPartParser,)
# 	)
# 	def avatar(self, request, pk=None):
# 		if request.method in ['POST', 'OPTION']:
# 			upload = request.FILES['avatar']
# 			if not upload:
# 				return Response(status=400)
#
# 			filename = 'myfile'
# 			with open(filename, 'wb+') as temp_file:
# 				for chunk in upload.chunks():
# 					temp_file.write(chunk)
# 			avatar = open(filename)  # there you go
# 			new_avatar = Avatar(full_image=avatar)
# 			new_avatar.save()
# 			return Response(status=200)
# 		else:
# 			avatar = request.user.avatar
# 			serializer = AvatarSerializer(avatar)
# 			return Response(serializer.data)


class AccountMe(generics.GenericAPIView):
	serializer_class = AccountSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Account.objects.filter(pk=self.request.user.pk)







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
