from model import Moment
from rest_framework import serializers

from ..comments.model import Comment


class MomentSerializer(serializers.ModelSerializer):
	creator = serializers.ReadOnlyField(source='creator.username')
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all(), required=False)

	class Meta:
		model = Moment
		fields = ('id', 'content', 'images', 'creator', 'comments')

	def perform_create(self, serializer):
		serializer.save(creator=self.request.user)


