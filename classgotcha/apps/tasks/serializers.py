from model import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'task_name', 'task_des', 'start', 'end',
		          'due_date', 'type', 'involved', 'classroom', 'group')
