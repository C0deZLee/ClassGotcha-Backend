from models import Classroom, Major, OfficeHour
from rest_framework import serializers

from ..tasks.serializers import ClassTimeTaskSerializer
from ..accounts.serializers import BasicAccountSerializer, ProfessorSerializer, SemesterSerializer, BasicProfessorSerializer
from ..tags.serializers import ClassFolderSerializer


class MajorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Major
		fields = '__all__'


class BasicClassroomSerializer(serializers.ModelSerializer):
	students_count = serializers.ReadOnlyField()
	class_short = serializers.ReadOnlyField()
	class_time = ClassTimeTaskSerializer()
	semester = SemesterSerializer()
	professors = BasicProfessorSerializer(many=True)

	class Meta:
		model = Classroom
		fields = ('id', 'class_code', 'class_short', 'students_count',
		          'class_section', 'description', 'class_time', 'semester', 'professors')


class ClassroomSerializer(serializers.ModelSerializer):
	class_time = ClassTimeTaskSerializer()
	students = BasicAccountSerializer(many=True)
	# groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	students_count = serializers.ReadOnlyField()
	class_short = serializers.ReadOnlyField()
	folders = ClassFolderSerializer(many=True)
	semester = SemesterSerializer()
	major = MajorSerializer()
	professors = BasicProfessorSerializer(many=True)

	class Meta:
		model = Classroom
		fields = '__all__'


class OfficeHourSerializer(serializers.ModelSerializer):
	professors = ProfessorSerializer(many=True)
	time = ClassTimeTaskSerializer()

	class Meta:
		model = OfficeHour
		fields = '__all__'
