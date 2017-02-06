from models import Task
from rest_framework import serializers


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
		# don't change here
		if 'involved' in validated_data and validated_data['involved'] == []:
			del validated_data['involved']

		# {'classroom': 4545, u'type': 1, u'description': u'hw1', u'task_name': u'hw1',
		# u'due': datetime.datetime(2017, 1, 30, 15, 24)}

		# create a empty instance first so we have pk and can add m2m relations
		task = Task.objects.create()
		# put value in
		Task.objects.filter(pk=task.pk).update(**validated_data)
		# don't know why but add this line then work
		task = Task.objects.get(pk=task.pk)

		if task.classroom:
			for student in task.classroom.students.all():
				task.involved.add(student)
			task.save()
		elif task.group:
			for member in task.group.members.all():
				task.involved.add(member)
			task.save()
		return task


class BasicTaskSerializer(serializers.ModelSerializer):
	formatted_start_time = serializers.ReadOnlyField()
	formatted_end_time = serializers.ReadOnlyField()
	formatted_start_date = serializers.ReadOnlyField()
	formatted_end_date = serializers.ReadOnlyField()
	repeat_start_date = serializers.ReadOnlyField()
	repeat_end_date = serializers.ReadOnlyField()
	repeat_list = serializers.ReadOnlyField()

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
		          'id')


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
