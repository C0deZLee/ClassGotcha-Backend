from rest_framework import serializers

from models import Account, Avatar, Group, Professor
from ..chat.models import Room
from ..classrooms.models import Semester, Classroom, Major, OfficeHour
from ..tasks.serializers import BasicTaskSerializer, ClassTimeTaskSerializer
from ..tags.serializers import ClassFolderSerializer

from ..matrix.client import MatrixClient
from ...settings.production import MATRIX_HOST

# Due to the cross dependency,
# I have to move SemesterSerializer, MajorSerializer and BasicClassroomSerializer here

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


class AvatarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = ('avatar2x', 'avatar1x')


class BasicProfessorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Professor
		fields = '__all__'
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
	avatar = AvatarSerializer(required=False)
	full_name = serializers.ReadOnlyField()

	class Meta:
		model = Account
		fields = ('pk', 'id', 'avatar', 'username', 'email', 'full_name', 'about_me', 'level')


# WARN: Duplicate
class RoomSerializer(serializers.ModelSerializer):
	latest_message = serializers.ReadOnlyField()
	accounts = BasicAccountSerializer(many=True)
	creator = BasicAccountSerializer()

	class Meta:
		model = Room
		fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
	classrooms = BasicClassroomSerializer(many=True)
	is_professor = serializers.ReadOnlyField()
	full_name = serializers.ReadOnlyField()
	tasks = BasicTaskSerializer(many=True)
	avatar = AvatarSerializer(required=False)

	class Meta:
		model = Account
		exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff',
		           'is_active', 'password', 'avatar')
		read_only_fields = ('created', 'updated',)


class AuthAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('username', 'email', 'password', 'first_name', 'last_name')
		write_only_fields = ('password',)

	def create(self, validated_data):
		#Client = MatrixClient(MATRIX_HOST,token = 'MDAyNGxvY2F0aW9uIG1hdHJpeC5jbGFzc2dvdGNoYS5jb20KMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDMxY2lkIHVzZXJfaWQgPSBAc2ltb3d1Om1hdHJpeC5jbGFzc2dvdGNoYS5jb20KMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSBVUE1BZThKK2owc1F4OSxxCjAwMmZzaWduYXR1cmUg83EO7apwt7bOwIdduNoS9HKKZhDvSnwi1pDRWjBXlxYK',user_id = '@simowu:matrix.classgotcha.com')
		#print Client.get_rooms()
		Client = MatrixClient("http://localhost:8007")
		token = Client.register_with_password(username="foobar",
            password="monkey")
		print token
		account = Account(email=validated_data['email'], username=validated_data['username'],
		                  first_name=validated_data['first_name'], last_name=validated_data['last_name'])
		account.set_password(validated_data['password'])
		token = Client.register_with_password(validated_data['username'], validated_data['password'])
		account.matrix_token = token
		account.save()
		return account


class GroupSerializers(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('group_type', 'members', 'classroom', 'creator')
