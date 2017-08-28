# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from serializers import Chatroom, ChatroomSerializer
from ..accounts.models import Account
from ..classrooms.models import Classroom
from matrix.matrix_api import MatrixApi


class ChatroomViewSet(viewsets):
	queryset = Chatroom.objects.all()
	serializer_class = ChatroomSerializer
	permission_classes = (IsAuthenticated,)

	def retrieve(self, request, pk):
		chatroom = get_object_or_404(self.queryset, pk=pk)
		serializer = ChatroomSerializer(chatroom)
		return Response(serializer.data)

	def create(self, request):
		"""Create Chatroom
			request.data:
			invitees(list<str>): Required, list of account id
			name(str): Required
			room_type(int): Required
			classroom_id(int): Required if room_type is 0
		"""
		if 'invitees' not in request.data:
			return Response({'error': 'No invitees found.'}, status=status.HTTP_400_BAD_REQUEST)
		if 'name' not in request.data:
			return Response({'error': 'No name found.'}, status=status.HTTP_400_BAD_REQUEST)
		if 'room_type' not in request.data:
			return Response({'error': 'No room_type found.'}, status=status.HTTP_400_BAD_REQUEST)
		if request.data['room_type'] == 0 and 'classroom_id' not in request.data:
			return Response({'error': 'No classroom_id found.'}, status=status.HTTP_400_BAD_REQUEST)

		matrix_token = request.user.matrix_token
		matrix = MatrixApi(auth_token=matrix_token)
		room_id = matrix.create_room(name=request.data['name'])

		# if classroom (type=0)
		if request.data['room_type'] == 0:
			chatroom = Chatroom.objects.create(matrix_id=room_id, room_name=request.data['name'], room_type=0,
			                                   classroom_id=int(request.data['classroom_id']))
			chatroom.save()
			for user_id in request.data['invitees']:
				# TODO: invited but not accepted, need NOTIFICATION
				chatroom.invitees.add(Account.objects.get(id=user_id))
			chatroom.save()

		# if private (type=1)
		if request.data['room_type'] == 1:
			chatroom = Chatroom.objects.create(matrix_id=room_id, room_name=request.data['name'], room_type=1,
			                                   admin_id=request.user.id)
			chatroom.save()
			for user_id in request.data['invitees']:
				# TODO: invited but not accepted, need NOTIFICATION
				chatroom.invitees.add(Account.objects.get(id=user_id))
			chatroom.save()

		# if one on one (type=2)
		if request.data['room_type'] == 2:
			# TODO: how to solve one on one chatting
			pass

		return Response(status=status.HTTP_201_CREATED)

	def join(self, request):
		"""Join Chatroom
			request.data:
			room_id(str): Required
		"""
		if 'room_id' not in request.data:
			return Response({'error': 'No room_id found.'}, status=status.HTTP_400_BAD_REQUEST)

		matrix_token = request.user.matrix_token
		matrix = MatrixApi(auth_token=matrix_token)
		# if join successful
		if matrix.join_room(request.data['room_id']):
			chatroom = Chatroom.objects.get(room_id=request.data['room_id'])
			chatroom.members.add(request.user)
			chatroom.invitees.remove(request.user)
			chatroom.save()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def invite(self, request):
		"""Invite user
			request.data:
			room_id(str): Required
			invitee(int): Required if method is POST
		"""
		# get current invitations
		if request.method == 'GET':
			pass

		# invite users
		if request.method == 'POST':
			pass

		# accept invitation
		if request.method == 'PUT':
			pass

