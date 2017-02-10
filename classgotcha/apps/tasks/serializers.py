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

	class Meta:
		model = Task
		fields = '__all__'

	def create(self, validated_data):
		# if no involved
		if 'involved' in validated_data and validated_data['involved'] == []:
			# TODO: deal with involved later on
			del validated_data['involved']

		# create a empty instance first so we have pk and can add m2m relations
		task = Task.objects.create()
		# put value in
		Task.objects.filter(pk=task.pk).update(**validated_data)
		# don't know why but add this line then work
		task = Task.objects.get(pk=task.pk)

		if task.classroom:
			task.involved.add(*task.classroom.students.all())
		elif task.group:
			task.involved.add(*task.group.members.all())

		return task


class BasicTaskSerializer(serializers.ModelSerializer):
	formatted_start_time = serializers.ReadOnlyField()
	formatted_end_time = serializers.ReadOnlyField()
	formatted_start_date = serializers.ReadOnlyField()
	formatted_end_date = serializers.ReadOnlyField()
	repeat_start_date = serializers.ReadOnlyField()
	repeat_end_date = serializers.ReadOnlyField()
	repeat_list = serializers.ReadOnlyField()
	classroom = TaskClassroomSerializer()
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
		          'task_name',
		          'type',
		          'description',
		          'category',
		          'location',
		          'start',
		          'end',
		          'id',
		          'classroom',
		          'expired')


'''
The serializer for showing class schedule
'''


class ClassTimeTaskSerializer(serializers.ModelSerializer):
	formatted_start_time = serializers.ReadOnlyField()
	formatted_end_time = serializers.ReadOnlyField()
	repeat_start_date = serializers.ReadOnlyField()
	repeat_end_date = serializers.ReadOnlyField()
	repeat_list = serializers.ReadOnlyField()

	class Meta:
		model = Task
		fields = ('formatted_start_time', 'formatted_end_time', 'repeat_start_date',
		          'repeat_end_date', 'repeat_list', 'task_name', 'location', 'repeat')
