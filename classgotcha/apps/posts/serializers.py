from models import Moment, Comment, Post
from rest_framework import serializers


class MomentSerializer(serializers.ModelSerializer):
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all(), required=False)

	class Meta:
		model = Moment
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'


