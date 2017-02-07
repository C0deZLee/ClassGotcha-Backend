from models import Room, Message
from rest_framework import serializers
from ..accounts.serializers import BasicAccountSerializer


class RoomSerializer(serializers.ModelSerializer):
	latest_message = serializers.ReadOnlyField()
	accounts = BasicAccountSerializer(many=True)
	creator = BasicAccountSerializer()

	class Meta:
		model = Room
		fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
	send_from = BasicAccountSerializer

	class Meta:
		model = Message
		fields = '__all__'
		read_only_fields = ('created',)
