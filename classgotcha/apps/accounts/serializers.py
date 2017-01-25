from models import Account, Avatar
from rest_framework import serializers

from ..posts.serializers import Moment, MomentSerializer
from ..notes.serializers import Note, NoteSerializer
from ..chat.serializers import Message, MessageSerializer
from ..classrooms.serializers import BasicClassroomSerializer

import random


class AccountSerializer(serializers.ModelSerializer):
	friends = serializers.PrimaryKeyRelatedField(
		many=True, queryset=Account.objects.filter())

	classrooms = serializers.StringRelatedField(many=True, read_only=True)
	moments = serializers.PrimaryKeyRelatedField(
		many=True, queryset=Moment.objects.exclude(flagged_num=3))
	# however this nested way always encounters problem
	# moments = MomentSerializer(read_only = True)

	notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	# classroom = BasicClassroomSerializer(many = True, read_only = True)
	# messages = MessageSerializer(many = True , read_only = True)
	recievedMessages = serializers.PrimaryKeyRelatedField(
		many=True, queryset=Message.objects.all())

	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff',
		           'is_student', 'is_professor', 'is_active', 'password')
		read_only_fields = ('is_student', 'is_professor',
		                    'created', 'updated',)


class BasicAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser',
		           'is_staff', 'is_active', 'password')
		read_only_fields = ('is_student', 'is_professor',
		                    'created', 'updated',)


class AuthAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('username', 'email', 'password')
		write_only_fields = ('password',)

	def create(self, validated_data):
		account = Account(email=validated_data[
			'email'], username=validated_data['username'])
		account.set_password(validated_data['password'])
		# account.avatar = Avatar.objects.get(pk=random.randint(1, 10))
		account.avatar = Avatar.objects.get(pk=1)
		account.save()
		return account


class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = '__all__'
		read_only_fields = ('created',)
