from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from serializers import RoomSerializer
from models import Room

from ..accounts.serializers import Account, BasicAccountSerializer


class ChatRoomViewSet(viewsets.ViewSet):
	queryset = Room.objects.all()
	# parser_classes = (FormParser, MultiPartParser,)
	permission_classes = (IsAuthenticated,)

	def create(self, request):
		room = Room.objects.create()
		room.accounts.add(request.user)
		room.creator = request.user
		user_list = request.data.get('user_list', [])
		for user_id in user_list:
			user = get_object_or_404(Account, pk=user_id)
			room.accounts.add(user)
		room.save()
		serializer = RoomSerializer(room)
		return Response(serializer.data)

	def retrieve(self, request, pk):
		room = get_object_or_404(self.queryset, pk=pk)
		serializer = RoomSerializer(room)
		return Response(serializer.data)

	'''
	Get users in chat current room
	'''

	def users(self, request, pk):
		room = get_object_or_404(self.queryset, pk=pk)
		if request.user in room.accounts.all():
			serializer = BasicAccountSerializer(room.accounts.all(), many=True)
			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)

	def validate(self, request, pk):
		room = get_object_or_404(self.queryset, pk=pk)
		if request.user in room.accounts.all():
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def latest_message(self, request, pk):
		room = get_object_or_404(self.queryset, pk=pk)
		return room.latest_message
