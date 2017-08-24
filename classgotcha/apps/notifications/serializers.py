from rest_framework import serializers

from models import Notification
from ..accounts.serializers import BasicAccountSerializer


class NotificationSerializer(serializers.ModelSerializer):
	receiver = BasicAccountSerializer()
	sender = BasicAccountSerializer()

	class Meta:
		model = Notification
		fields = ('id', 'send_from', 'content', 'read', 'created', 'receiver', 'sender')
