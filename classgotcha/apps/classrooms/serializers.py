from models import Classroom
from rest_framework import serializers
from ..groups.models import Group
from ..tasks.models import Task


class ClassroomSerializer(serializers.ModelSerializer):
	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	students_count = serializers.ReadOnlyField()

	class Meta:
		model = Classroom
		fields = '__all__'


class BasicClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ('students', 'updated', 'syllabus')
