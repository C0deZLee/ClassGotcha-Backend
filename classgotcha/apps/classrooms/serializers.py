from model import Classroom
from rest_framework import serializers
from ..groups.model import Group
from ..tasks.model import Task


class ClassroomSerializer(serializers.ModelSerializer):
	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())

	class Meta:
		model = Classroom
		fields = ('id', 'class_name', 'class_number', 'class_code', 'syllabus',
		          'description', 'professor', 'major', 'students', 'tasks', 'groups')


class BasicClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ('id', 'class_name', 'class_number', 'class_code', 'syllabus',
		          'description', 'professor', 'major')
