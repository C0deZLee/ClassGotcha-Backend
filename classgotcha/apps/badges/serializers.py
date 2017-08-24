from rest_framework import serializers

from models import BadgeType, Badge


class BadgeTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = BadgeType
		fields = ('name', 'action_required', 'description', 'level', 'identifier')


class BadgeSerializer(serializers.ModelSerializer):
	badge_type = BadgeTypeSerializer()

	class Meta:
		model = Badge
		fields = ('counter', 'started', 'finished', 'badge_type')
