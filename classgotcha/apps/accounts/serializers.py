from models import Account, Avatar
from rest_framework import serializers
# from ..classrooms.models import Classroom
from ..posts.models import Moment
# from ..groups.models import Group
from ..notes.models import Note
# from ..posts.models import Moment, Post
# from ..tasks.models import Task
import random

class AccountSerializer(serializers.ModelSerializer):
	friends = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())
	# classrooms = serializers.StringRelatedField(many=True, read_only=True)
	moments = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.exclude(flagged_num=3))
	notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
	# tasks
	# messages

	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff', 'is_active', 'password')
		read_only_fields = ('is_student', 'is_professor', 'created', 'updated',)


class BasicAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff', 'is_active', 'password')
		read_only_fields = ('is_student', 'is_professor', 'created', 'updated',)


class AuthAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('username', 'email', 'password')
		write_only_fields = ('password',)

	def create(self, validated_data):
		account = Account(email=validated_data['email'], username=validated_data['username'])
		account.set_password(validated_data['password'])
		account.avatar = Avatar.objects.get(pk = random.randint(1,10))
		account.save()
		return account


class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = ('full_image', 'thumbnail', 'created')
		read_only_fields = ('created',)

	#def create(self,validated_data):



