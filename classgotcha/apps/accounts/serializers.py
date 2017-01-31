from models import Account, Avatar, Group, Professor
from rest_framework import serializers
from ..tasks.serializers import BasicTaskSerializer


# try:
# 	from ..posts.serializers import MomentSerializer
# except ImportError:
# 	import sys
# 	MomentSerializer = sys.modules['classgotcha.apps.posts.serializers.MomentSerializer']

# from ..posts.serializers import Moment, MomentSerializer
# from ..notes.serializers import Note, NoteSerializer
# from ..chat.serializers import Message, MessageSerializer
# from ..classrooms.serializers import BasicClassroomSerializer
# import random


class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = '__all__'
		read_only_fields = ('created',)


class AccountSerializer(serializers.ModelSerializer):
	# friends = serializers.PrimaryKeyRelatedField(
	# 	many=True, queryset=Account.objects.filter())
	#
	# classrooms = serializers.StringRelatedField(many=True, read_only=True)
	# moments = MomentSerializer(many=True)
	# 	many=True, queryset=Moment.objects.exclude(flagged_num=3))
	# # however this nested way always encounters problem
	# # moments = MomentSerializer(read_only = True)
	#
	# notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	# tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	# classroom = BasicClassroomSerializer(many = True, read_only = True)
	# messages = MessageSerializer(many = True , read_only = True)
	# receivedMessages = serializers.PrimaryKeyRelatedField()
	# many=True, queryset=Message.objects.all())
	tasks = BasicTaskSerializer(many=True)
	avatar = AvatarSerializer(required=False)
	is_professor = serializers.SerializerMethodField()
	full_name = serializers.SerializerMethodField()

	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff',
		           'is_active', 'password', 'avatar')
		read_only_fields = ('created', 'updated',)

	def get_is_professor(self, obj):
		return obj.is_professor

	def get_full_name(self, obj):
		return obj.get_full_name


class BasicAccountSerializer(serializers.ModelSerializer):
	avatar = AvatarSerializer(required=False)
	full_name = serializers.SerializerMethodField()

	class Meta:
		model = Account
		fields = ('pk', 'id', 'avatar', 'username', 'email', 'full_name', 'about_me', 'level')

	def get_full_name(self, obj):
		return obj.first_name + ' ' + obj.last_name


class AuthAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('username', 'email', 'password', 'first_name', 'last_name')
		write_only_fields = ('password',)

	def create(self, validated_data):
		account = Account(email=validated_data['email'], username=validated_data['username'],
		                  first_name=validated_data['first_name'], last_name=validated_data['last_name'])
		account.set_password(validated_data['password'])
		account.save()
		return account


class GroupSerializers(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('group_type', 'members', 'classroom', 'creator')


class ProfessorSerializers(serializers.ModelSerializer):
	full_name = serializers.ReadOnlyField()
	class Meta:
		model = Professor
		fields = '__all__'
		read_only_fields = ('created',)
