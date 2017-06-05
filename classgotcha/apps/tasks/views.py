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
		print pk, "wocaonima"

		task = get_object_or_404(self.queryset, pk=pk)
		for (key, value) in request.data.items():
			if key in ['task_name', 'description', 'start', 'end', 'location', 'category', 'repeat']:
				setattr(task, key, value)
		task.save()

		if task.classroom:
			Moment.objects.create(
				content='I just updated the task \"' +
				        request.data.get('task_name', '') + '\" to the classroom, check it out!',
				creator=request.user,
				classroom=task.classroom)
		return Response(status=status.HTTP_200_OK)

	def delete(self, request, pk):
		task = get_object_or_404(self.queryset, pk=pk)
		task.delete()
		return Response(status=status.HTTP_200_OK)
