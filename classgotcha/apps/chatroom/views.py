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

	'''
	request.data:
	invitees(list<str>): Required
	name(str): Required
	room_type(int): Required
	classroom_id(int): Optional. Required if room_type is 0
	'''

	def create(self, request):
		if "invitees" not in request.data:
			return Response({'error': 'No invitees found.'}, status=status.HTTP_400_BAD_REQUEST)
		if 'name' not in request.data:
			return Response({'error': 'No name found.'}, status=status.HTTP_400_BAD_REQUEST)
		if 'room_type' not in request.data:
			return Response({'error': 'No room_type found.'}, status=status.HTTP_400_BAD_REQUEST)
		if request.data['room_type'] == 0 and 'classroom_id' not in request.data:
			return Response({'error': 'No classroom_id found.'}, status=status.HTTP_400_BAD_REQUEST)

		matrix_token = request.user.matrix_token
		matrix = MatrixApi(auth_token=matrix_token)
		invitees = []

		for user_id in request.data['invitees']:
			invitees.append(Account.objects.get(id=user_id).matrix_id)

		room_id = matrix.create_room(name=request.data['name'], invitees=invitees)

		# If classroom
		if request.data['room_type'] == 0:
			chatroom = Chatroom.objects.create(matrix_id=room_id, room_name=request.data['name'],
			                                   classroom_id=request.data['classroom_id'])

			chatroom.save()

		return Response(status=status.HTTP_200_OK)

	#
	#
	#
 	# matrix_id = models.CharField(max_length=200)
	# room_name = models.CharField(max_length=200)
	# room_type = models.IntegerField(default=class_room, choices=type_choices)
	#
	# # Relations
	# classroom = models.ForeignKey(Classroom, related_name='chatrooms', null=True)
	# creator = models.ForeignKey(Account, related_name='created_chatrooms')
	# # Timestamp
	# created = models.DateTimeField(auto_now_add=True)