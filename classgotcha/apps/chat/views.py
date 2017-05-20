from  datetime import datetime

from django.shortcuts import get_object_or_404
from django.core.files.base import File

from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..classrooms.serializers import Classroom, BasicClassroomSerializer
from ..posts.serializers import Moment, MomentSerializer, NoteSerializer, Comment, CommentSerializer
from ..chat.serializers import RoomSerializer
from ..tasks.serializers import TaskSerializer

from ..posts.models import Rate
from models import Account, Avatar, Professor
from serializers import AccountSerializer, BasicAccountSerializer, AuthAccountSerializer, AvatarSerializer, \
	ProfessorSerializer
import requests


class ChatViewSet(viewsets.Viewset):
	queryset = Account.objects.exclude(is_staff=1)
	parser_classes = (MultiPartParser, FormParser, JSONParser)
	permission_classes = (IsAuthenticated,)

	def create_private_group_chat(self,request,pks): #can pass a list of pk?
		# create a new matrix chat room if not exists
		room_name_list = []
		# get all user names
		for pk in pks:
			user = get_object_or_404(self.queryset, pk=pk)
			room_name_list.append(user.username)
		# just combine all the username?
		

		# sort the room_name_list and then combine all?
		try:
			r = requests.post('http://matrix.classgotcha.com:8008/_matrix/client/r0/createRoom',json = {"preset":"public_chat","room_alis_name":cours['name'] + ' - ' + cours['section'] + ' Chat Room' ,"name":cours['name'] + ' - ' + cours['section'] + ' Chat Room',"topic":"classroom chat","creation_content":{"m.federate":False}},headers = {"Content-Type":"application/json"},params = {"access_token":request.user.matrix_token})
					room_id = r.json()['room_id']
		except:
			pass # need to make sure in this case the room is already existing
		Room.objects.create(creator=Account.objects.get(is_superuser=True),
										room_type = "Classroom",room_id = room_id,
					                    name=cours['name'] + ' - ' + cours['section'] + ' Chat Room',
					                    classroom=classroom)


