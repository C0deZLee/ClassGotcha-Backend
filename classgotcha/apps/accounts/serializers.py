from models import Account, Avatar
from rest_framework import serializers
# from ..classrooms.models import Classroom
# from ..comments.models import Comment
# from ..groups.models import Group
# from ..notes.models import Note
# from ..posts.models import Moment, Post
# from ..tasks.models import Task


# class AccountSerializer(serializers.ModelSerializer):
# 	friends = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())
# 	teaches = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all())
# 	classrooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all())
# 	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
# 	joined_groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
# 	created_groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
# 	notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
# 	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
# 	moments = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.all())
# 	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
#
# 	class Meta:
# 		model = Account
# 		fields = ('id', 'email', 'username',
# 		          'first_name', 'mid_name', 'last_name',
# 		          'gender', 'birthday', 'school_year',
# 		          'avatar', 'friends', 'major',
# 		          'teaches', 'classrooms', 'comments',
# 		          'joined_groups', 'created_groups',
# 		          'notes', 'posts', 'moments', 'tasks',)
# 		read_only_fields = ('is_admin', 'is_student', 'is_professor',
# 		                    'created', 'updated',)


class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id', 'email', 'username', 'password', 'first_name', 'mid_name', 'last_name',
		          'gender', 'birthday', 'school_year', 'major', 'avatar',
		          'is_admin', 'is_student', 'is_professor', 'created', 'updated',)
		read_only_fields = ('is_admin', 'is_student', 'is_professor', 'created', 'updated',)
		write_only_fields = ('password',)

	def create(self, validated_data):
		account = Account(email=validated_data['email'], username=validated_data['username'])
		account.set_password(validated_data['password'])
		account.save()
		return account

	# only for updating password
	def update(self, instance, validated_data):
		if not validated_data['password']:
			# TODO: update profile
			instance.save()
		else:
			# instance.update
			instance.set_password(validated_data['password'])
			instance.save()
		return instance



class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = ('full_image', 'thumbnail', 'created')
		read_only_fields = ('created',)


# class AuthAccountSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Account
# 		fields = ('email', 'username')
# 		extra_kwargs = {'password': {'write_only': True}}
#
# 	def create(self, validated_data):
# 		account = Account(email=validated_data['email'], username=validated_data['username'])
# 		account.set_password(validated_data['password'])
# 		account.save()
# 		return account
#
# 	def change_password(self, instance, validated_data):
# 		instance.set_password(validated_data['password'])
# 		instance.save()
# 		return instance

