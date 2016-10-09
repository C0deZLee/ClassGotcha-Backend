from model import Moment, Comment
from rest_framework import serializers


class MomentSerializer(serializers.ModelSerializer):
	creator = serializers.ReadOnlyField(source='creator.username')

	class Meta:
		model = Moment
		fields = ('id', 'content', 'images', 'creator')

	def perform_create(self, serializer):
		serializer.save(creator=self.request.user)


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'content', 'images', 'creator', 'belongs_to')
