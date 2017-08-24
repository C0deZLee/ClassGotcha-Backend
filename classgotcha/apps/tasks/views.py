from datetime import datetime
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..posts.serializers import MomentSerializer, Moment
from serializers import Task


class TaskViewSet(viewsets.ViewSet):
	queryset = Task.objects.all()
	serializer_class = MomentSerializer
	permission_classes = (IsAuthenticated,)

	def add(self, request, pk):
		task = get_object_or_404(self.queryset, pk=pk)
		task.involved.add(request.user)
		return Response(status=status.HTTP_200_OK)

	def update(self, request, pk):
		task = get_object_or_404(self.queryset, pk=pk)

		# Personal task
		if task.category == 6 and task.creator_id == request.user.id:
			try:
				if request.data['repeat']:
					start = datetime.strptime(request.data['formatted_start_time'], '%H:%M:%S')
					task.start = start
					end = datetime.strptime(request.data['formatted_end_time'], '%H:%M:%S')
					task.end = end
					task.repeat = request.data['repeat']
					task.location = request.data['location']
					task.task_name = request.data['task_name']
					task.save()
				else:
					task.repeat = ''
					start = datetime.strptime(request.data['formatted_start_datetime'], '%Y-%m-%dT%H:%M:%S')
					task.start = start
					end = datetime.strptime(request.data['formatted_end_datetime'], '%Y-%m-%dT%H:%M:%S')
					task.end = end
					task.location = request.data['location']
					task.task_name = request.data['task_name']
					task.save()
			except:
				return Response({'detail': 'Wrong Time Format.'}, status=status.HTTP_400_BAD_REQUEST)

		# Classroom or public task
		if task.task_of_classroom in request.user.classrooms.all():
			for (key, value) in request.data.items():
				if key in ['task_name', 'description', 'start', 'end', 'location', 'category', 'repeat']:
					setattr(task, key, value)
			task.save()

		if task.task_of_classroom:
			Moment.objects.create(
				content='I updated the task \"' +
				        request.data.get('task_name', '') + '\", check it out!',
				creator=request.user,
				classroom_id=task.task_of_classroom_id)

		return Response(status=status.HTTP_200_OK)

	def delete(self, request, pk):
		task = get_object_or_404(self.queryset, pk=pk)

		if task.category == 6 and task.creator_id == request.user.id:
			task.delete()
		else:
			task.involved.remove(request.user)

		return Response(status=status.HTTP_200_OK)
