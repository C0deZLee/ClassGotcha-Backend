from models import Account, Avatar
from rest_framework import serializers
from ..classrooms.models import Classroom
from ..posts.models import Moment
# from ..groups.models import Group
from ..notes.models import Note
# from ..posts.models import Moment, Post
# from ..tasks.models import Task


class AccountSerializer(serializers.ModelSerializer):

	friends = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())
	classrooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all())
	moments = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.exclude(flagged_num=3))
	notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff', 'is_active')
		read_only_fields = ('is_student', 'is_professor', 'created', 'updated',)
		write_only_fields = ('password',)

	def create(self, validated_data):
		account = Account(email=validated_data['email'], username=validated_data['username'])
		account.set_password(validated_data['password'])
		account.save()
		return account


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
		account.save()
		return account


class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = ('full_image', 'thumbnail', 'created')
		read_only_fields = ('created',)


