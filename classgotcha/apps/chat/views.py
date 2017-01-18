from haikunator import Haikunator

from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, api_view, permission_classes, parser_classes
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser

from serializers import RoomSerializer, MessageSerializer
from models import Room

from ..accounts.serializers import AccountSerializer


def rooms(request, template="rooms.html"):
	"""
	Homepage - lists all rooms.
	"""
	context = {"rooms": Room.objects.all()}
	return render(request, template, context)


def about(request):
	return render(request, "about.html")


def new_room(request):
	"""
	Randomly create a new room, and redirect to it.
	"""
	new_room = None
	while not new_room:
		with transaction.atomic():
			label = Haikunator.haikunate(Haikunator())

			if Room.objects.filter(label=label).exists():
				continue
			new_room = Room.objects.create(label=label)
	return redirect(chat_room, label=label)


def chat_room(request, label):
	# If the room with the given label doesn't exist, automatically create it
	# upon first visit (a la etherpad).
	room, created = Room.objects.get_or_create(label=label)

	# We want to show the last 50 messages, ordered most-recent-last
	messages = reversed(room.messages.order_by('-timestamp')[:50])

	return render(request, "room.html", {
		'room': room,
		'messages': messages,
	})

	return Response({'room': room, 'messages': messages})


class ChatRoomViewSet(viewsets.ViewSet):
	queryset = Room.objects.all()
	# parser_classes = (FormParser, MultiPartParser,)
	permission_classes = (IsAuthenticated,)

	def create(self, request):
		room = Room.objects.create()
		room.accounts.add(request.user)
		room.creator = request.user
		room.save()
		serializer = RoomSerializer(room)
		return Response(serializer.data)

	def retrieve(self, request, pk):
		room = get_object_or_404(self.queryset, pk=pk)
		serializer = RoomSerializer(room)
		return Response(serializer.data)

	'''
	Get users in chat room
	'''
	def users(self, request, pk):
		room = get_object_or_404(self.queryset, pk=pk)
		serializer = AccountSerializer(room.accounts.all(), many=True)
		return Response(serializer.data)

	def join(self, request, pk):
		room = get_object_or_404(self.queryset, pk=pk)
		room.accounts.add(request.user)
		room.save()
		return Response(status=status.HTTP_200_OK)

	def send(self, request, pk):
		pass
