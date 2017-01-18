from models import Room, Message
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Room
		fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'
		read_only_fields = 'created'
