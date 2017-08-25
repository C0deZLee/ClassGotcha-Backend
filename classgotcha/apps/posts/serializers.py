from models import Moment, Comment, Post, Note
from ..accounts.serializers import BasicAccountSerializer
from ..tags.serializers import BasicTagSerializer
from ..classrooms.serializers import MiniClassroomSerializer
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
	creator = BasicAccountSerializer(required=False)

	class Meta:
		model = Comment
		fields = '__all__'


class MomentSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(required=False, many=True)
	classroom = MiniClassroomSerializer(required=False)
	creator = BasicAccountSerializer(required=False)
	likes = serializers.SerializerMethodField()

	class Meta:
		model = Moment
		fields = '__all__'

	def get_likes(self, obj):
		return obj.likes


class PostSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(required=False, many=True)
	creator = BasicAccountSerializer(required=False)

	class Meta:
		model = Post
		fields = '__all__'


class BasicPostSerializer(serializers.ModelSerializer):
	creator = BasicAccountSerializer(required=False)

	class Meta:
		model = Post
		fields = ('id', 'title', 'comments', 'creator', 'created', 'votes', 'tag')


# from ..groups.models import Group
# from ..tasks.models import Task


class NoteSerializer(serializers.ModelSerializer):
	# tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	# groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	overall_rating = serializers.ReadOnlyField()
	creator = BasicAccountSerializer()
	tags = BasicTagSerializer(many=True)

	class Meta:
		model = Note
		fields = '__all__'
