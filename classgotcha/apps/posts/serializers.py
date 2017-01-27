from models import Moment, Comment, Post
from ..accounts.serializers import BasicAccountSerializer
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
	creator = BasicAccountSerializer(required=False)

	class Meta:
		model = Comment
		fields = '__all__'


class MomentSerializer(serializers.ModelSerializer):
	# comments = CommentSerializer(many=True, queryset=Comment.objects.all(), required=False)
	comments = CommentSerializer(required=False, many=True)
	creator = BasicAccountSerializer(required=False)
	likes = serializers.SerializerMethodField()

	class Meta:
		model = Moment
		fields = '__all__'

	def get_likes(self, obj):
		return obj.likes


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
