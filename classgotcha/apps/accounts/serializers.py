from rest_framework import serializers

from models import Account, Group, Professor
from ..chatrooms.models import Chatroom
from ..classrooms.models import Semester, Classroom, Major, OfficeHour
from ..tasks.serializers import BasicTaskSerializer, ClassTimeTaskSerializer
from ..tags.serializers import ClassFolderSerializer

from django.core.files.images import ImageFile


# from ..chatrooms.matrix.matrix_api import MatrixApi
# import requests


# Due to the cross dependency,
# I have to copy SemesterSerializer, MajorSerializer and BasicClassroomSerializer here

# WARN: Duplicate
class MajorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Major
		fields = '__all__'


# WARN: Duplicate
class SemesterSerializer(serializers.ModelSerializer):
	formatted_start_date = serializers.ReadOnlyField()
	formatted_end_date = serializers.ReadOnlyField()

	class Meta:
		model = Semester
		fields = ('name', 'formatted_start_date', 'formatted_end_date')


# class AvatarSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Account
# 		fields = ('avatar2x', 'avatar1x')


class BasicProfessorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Professor
		fields = ['full_name', 'email', 'id']
		read_only_fields = ('created',)


# WARN: Duplicate
class BasicClassroomSerializer(serializers.ModelSerializer):
	students_count = serializers.ReadOnlyField()
	class_short = serializers.ReadOnlyField()
	class_time = ClassTimeTaskSerializer()
	semester = SemesterSerializer()
	professors = BasicProfessorSerializer(many=True)
	folders = ClassFolderSerializer(many=True)

	class Meta:
		model = Classroom
		fields = ('id', 'class_code', 'class_short', 'students_count',
		          'class_section', 'description', 'class_time', 'semester', 'professors', 'folders')


class ProfessorOfficeHourSerializer(serializers.ModelSerializer):
	classroom = BasicClassroomSerializer()
	time = ClassTimeTaskSerializer()

	class Meta:
		model = OfficeHour
		fields = ('classroom', 'time')


class ProfessorSerializer(serializers.ModelSerializer):
	full_name = serializers.ReadOnlyField()
	classrooms = BasicClassroomSerializer(many=True)
	office_hours = ProfessorOfficeHourSerializer(many=True)
	avg_rate = serializers.ReadOnlyField()

	class Meta:
		model = Professor
		fields = '__all__'
		read_only_fields = ('created',)


class BasicAccountSerializer(serializers.ModelSerializer):
	full_name = serializers.ReadOnlyField()

	class Meta:
		model = Account
		fields = ('pk', 'id', 'avatar1x', 'avatar2x', 'username', 'email', 'full_name', 'about_me', 'level')


# WARN: Duplicate
# class RoomSerializer(serializers.ModelSerializer):
# 	latest_message = serializers.ReadOnlyField()
# 	accounts = BasicAccountSerializer(many=True)
# 	creator = BasicAccountSerializer()
#
# 	class Meta:
# 		model = Chatroom
# 		fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
	classrooms = BasicClassroomSerializer(many=True)
	is_professor = serializers.ReadOnlyField()
	full_name = serializers.ReadOnlyField()
	tasks = BasicTaskSerializer(many=True)

	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff',
		           'is_active', 'password',)
		read_only_fields = ('created', 'updated',)


class AuthAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('username', 'email', 'password', 'first_name', 'last_name')
		write_only_fields = ('password',)

	def create(self, validated_data):
		account = Account(email=validated_data['email'],
		                  username=validated_data['username'],
		                  first_name=validated_data['first_name'],
		                  last_name=validated_data['last_name'])

		account.set_password(validated_data['password'])

		# matrix = MatrixApi()
		# account.matrix_token = matrix.register(validated_data['username'], validated_data['password'])['access_token']
		# account.matrix_id =
		account.save()
		return account


class GroupSerializers(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('group_type', 'members', 'classroom', 'creator')
