from models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'

	def create(self, validated_data):
		# don't change here
		if 'involved' in validated_data and validated_data['involved'] == []:
			del validated_data['involved']
		# create a empty instance first so we have pk and can add m2m relations
		task = Task.objects.create()
		# put value in
		Task.objects.filter(pk=task.pk).update(**validated_data)
		# don't know why but add this line then work
		task = Task.objects.get(pk=task.pk)

		if task.classroom:
			print task.classroom
			for student in task.classroom.students.all():
				task.involved.add(student)
			task.save()
		elif task.group:
			for member in task.group.members.all():
				task.involved.add(member)
			task.save()
		return task

