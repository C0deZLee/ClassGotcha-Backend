from rest_framework import serializers

from models import Account, Avatar, Group, Professor
from ..chat.models import Room
from ..classrooms.models import Semester, Classroom
from ..tasks.serializers import BasicTaskSerializer, ClassTimeTaskSerializer


# Due to the cross dependency, i have to move SemesterSerializer and BasicClassroomSerializer here


class SemesterSerializer(serializers.ModelSerializer):
	formatted_start_date = serializers.ReadOnlyField()
	formatted_end_date = serializers.ReadOnlyField()

	class Meta:
		model = Semester
		fields = ('name', 'formatted_start_date', 'formatted_end_date')


class BasicClassroomSerializer(serializers.ModelSerializer):
	students_count = serializers.ReadOnlyField()
	class_short = serializers.ReadOnlyField()
	class_time = ClassTimeTaskSerializer()
	semester = SemesterSerializer()

	class Meta:
		model = Classroom
		fields = ('id', 'class_code', 'class_short', 'students_count',
		          'class_section', 'description', 'class_time', 'semester')


class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = '__all__'
		read_only_fields = ('created',)


class BasicAccountSerializer(serializers.ModelSerializer):
	avatar = AvatarSerializer(required=False)
	full_name = serializers.SerializerMethodField()

	class Meta:
		model = Account
		fields = ('pk', 'id', 'avatar', 'username', 'email', 'full_name', 'about_me', 'level')

	def get_full_name(self, obj):
		return obj.first_name + ' ' + obj.last_name


class RoomSerializer(serializers.ModelSerializer):
	latest_message = serializers.ReadOnlyField()
	accounts = BasicAccountSerializer(many=True)
	creator = BasicAccountSerializer()

	class Meta:
		model = Room
		fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
	classrooms = BasicClassroomSerializer(many=True)
	chatrooms = RoomSerializer(many=True)
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
