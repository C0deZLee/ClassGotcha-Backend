from models import Note
from rest_framework import serializers
# from ..groups.models import Group
# from ..tasks.models import Task


class NoteSerializer(serializers.ModelSerializer):
	# tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	# groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
	overall_rating = serializers.ReadOnlyField()

	class Meta:
		model = Note
		fields = '__all__'

#
# class BasicClassroomSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Classroom
# 		exclude = ('students', 'updated', 'syllabus')
