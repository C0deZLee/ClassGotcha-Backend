from models import Account
from rest_framework import serializers
from ..classrooms.models import Classroom
from ..comments.models import Comment
from ..groups.models import Group
from ..notes.models import Note
from ..posts.models import Moment, Post
from ..tasks.models import Task


class FullAccountSerializer(serializers.ModelSerializer):
	friends = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())
	teaches = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all())
	classrooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all())
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
	joined_groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	created_groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
	moments = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.all())
	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

	class Meta:
		model = Account
		fields = ('id', 'email', 'username',
		          'first_name', 'mid_name', 'last_name',
		          'gender', 'birthday', 'school_year',
		          'avatar', 'friends', 'major',
		          'teaches', 'classrooms', 'comments',
		          'joined_groups', 'created_groups',
		          'notes', 'posts', 'moments', 'tasks',)
		read_only_fields = ('is_admin', 'is_student', 'is_professor',
		                    'created', 'updated',)


class BaseAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id', 'email', 'username',
		          'first_name', 'mid_name', 'last_name',
		          'gender', 'birthday', 'school_year',
		          'major', 'avatar')
		read_only_fields = ('is_admin', 'is_student', 'is_professor',
		                    'created', 'updated',)


class AuthAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('email', 'username')
		extra_kwargs = {'password': {'write_only': True}}

	# def create(self, validated_data):
	# 	account = Account(email=validated_data['email'], username=validated_data['username'])
	# 	account.set_password(validated_data['password'])
	# 	account.save()
