from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..posts.serializers import MomentSerializer,  Moment
from serializers import Task


class TaskViewSet(viewsets.ViewSet):
	queryset = Task.objects.all()
	serializer_class = MomentSerializer
	permission_classes = (IsAuthenticated,)

	def update(self, request, pk):
		task = get_object_or_404(self.queryset, pk=pk)

		if (task.creator_id is request.user.id) or (task.task_of_classroom in request.user.classrooms.all()):
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
		task.delete()
		return Response(status=status.HTTP_200_OK)
