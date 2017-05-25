from models import Chatroom
from rest_framework import serializers


class ChatroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chatroom
		fields = '__all__'
