from models import Classroom, Semester, Major
from rest_framework import serializers

from ..tasks.serializers import BasicTaskSerializer
from ..accounts.serializers import BasicAccountSerializer

from ..groups.models import Group


class MajorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Major
		fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
	formatted_start_date = serializers.ReadOnlyField()
	formatted_end_date = serializers.ReadOnlyField()

	class Meta:
		model = Semester
		fields = ('name', 'formatted_start_date', 'formatted_end_date')


class ClassroomSerializer(serializers.ModelSerializer):
	class_time = BasicTaskSerializer()
	tasks = BasicTaskSerializer(many=True)
	students = BasicAccountSerializer(many=True)
	groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	students_count = serializers.ReadOnlyField()
	class_short = serializers.ReadOnlyField()
	semester = SemesterSerializer()
	major = MajorSerializer()

	class Meta:
		model = Classroom
		fields = '__all__'


class BasicClassroomSerializer(serializers.ModelSerializer):
	students_count = serializers.ReadOnlyField()
	class_short = serializers.ReadOnlyField()

	class Meta:
		model = Classroom
		fields = ('id', 'class_code', 'class_short', 'students_count', 'class_section', 'description')
