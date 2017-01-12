from models import Account, Avatar
from rest_framework import serializers
from ..classrooms.models import Classroom
# from ..comments.models import Comment
# from ..groups.models import Group
# from ..notes.models import Note
# from ..posts.models import Moment, Post
# from ..tasks.models import Task


class AccountSerializer(serializers.ModelSerializer):

	friends = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())
	classrooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all())

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


class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = ('full_image', 'thumbnail', 'created')
		read_only_fields = ('created',)


