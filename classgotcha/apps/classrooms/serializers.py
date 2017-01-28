from models import Classroom
from rest_framework import serializers

from ..tasks.serializers import BasicTaskSerializer
from ..accounts.serializers import BasicAccountSerializer

from ..groups.models import Group
from ..tasks.models import Task


class ClassroomSerializer(serializers.ModelSerializer):
	class_time = BasicTaskSerializer()
	tasks = BasicTaskSerializer(many=True)
	students = BasicAccountSerializer(many=True)
	groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	students_count = serializers.ReadOnlyField()
	class_short = serializers.ReadOnlyField()

	class Meta:
		model = Classroom
		fields = '__all__'


class BasicClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ('students', 'updated', 'syllabus')
