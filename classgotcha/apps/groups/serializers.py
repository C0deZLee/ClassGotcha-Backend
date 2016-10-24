from models import Group
from rest_framework import serializers


class GroupSerializers(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('group_type', 'members', 'classroom', 'creator')
