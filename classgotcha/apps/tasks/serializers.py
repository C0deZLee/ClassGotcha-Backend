from models import Task, Account
from rest_framework import serializers
from ..classrooms.models import Classroom


class TaskClassroomSerializer(serializers.ModelSerializer):
	class_short = serializers.ReadOnlyField()

	class Meta:
		model = Classroom
		fields = ('id', 'class_short',)


class TaskSerializer(serializers.ModelSerializer):
	formatted_start_time = serializers.ReadOnlyField()
	formatted_end_time = serializers.ReadOnlyField()
	formatted_start_datetime = serializers.ReadOnlyField()
	formatted_end_datetime = serializers.ReadOnlyField()
	repeat_start_date = serializers.ReadOnlyField()
	repeat_end_date = serializers.ReadOnlyField()
	repeat_list = serializers.ReadOnlyField()
	classroom = TaskClassroomSerializer(required=False)
	task_of_classroom = TaskClassroomSerializer(required=False)  # Classroom task

	class Meta:
		model = Task
		fields = '__all__'


class BasicTaskSerializer(serializers.ModelSerializer):
	formatted_start_time = serializers.ReadOnlyField()
	formatted_end_time = serializers.ReadOnlyField()
	formatted_start_date = serializers.ReadOnlyField()
	formatted_end_date = serializers.ReadOnlyField()
	repeat_start_date = serializers.ReadOnlyField()
	repeat_end_date = serializers.ReadOnlyField()
	repeat_list = serializers.ReadOnlyField()
	classroom = TaskClassroomSerializer(required=False)  # Classroom time
	task_of_classroom = TaskClassroomSerializer(required=False)  # Classroom task
	expired = serializers.ReadOnlyField()

	class Meta:
		model = Task
		fields = ('formatted_start_time',
		          'formatted_end_time',
		          'formatted_start_date',
		          'formatted_end_date',
		          'repeat_start_date',
		          'repeat_end_date',
		          'repeat_list',
		          'repeat',
		          'task_name',
		          'type',
		          'description',
		          'category',
		          'location',
		          'start',
		          'end',
		          'id',
		          'classroom',
		          'task_of_classroom',
		          'expired')


class ClassTimeTaskSerializer(serializers.ModelSerializer):
	'''
	The serializer for showing class schedule
	'''
	formatted_start_time = serializers.ReadOnlyField()
	formatted_end_time = serializers.ReadOnlyField()
	repeat_start_date = serializers.ReadOnlyField()
	repeat_end_date = serializers.ReadOnlyField()
	repeat_list = serializers.ReadOnlyField()

	class Meta:
		model = Task
		fields = ('formatted_start_time',
		          'formatted_end_time',
		          'repeat_start_date',
		          'repeat_end_date',
		          'repeat_list',
		          'task_name',
		          'location',
		          'repeat')


class CreateTaskSerializer(serializers.ModelSerializer):
	'''
	The serializer for create tasks
	'''

	class Meta:
		model = Task
		fields = '__all__'

	def create(self, validated_data):
		# if no involved
		# if 'involved' in validated_data and validated_data['involved'] == []:
		# 	# deal with involved later on
		# 	del validated_data['involved']

		task = Task.objects.create(**validated_data)

		# TODO: Task add to all classroom users immediately
		if task.task_of_classroom_id:
			task.involved.add(*task.task_of_classroom.students.all())

		elif task.group:
			task.involved.add(*task.group.members.all())

		return task
