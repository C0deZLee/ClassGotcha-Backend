from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from models import Notification
from serializers import NotificationSerializer


class NotificationViewSet(viewsets.ViewSet):
	queryset = Notification.objects.exclude(read=True)
	serializer_class = NotificationSerializer
	# Permission set
	permission_classes = (permissions.IsAuthenticated,)

	def fetch(self, request):
		notifications = self.queryset.filter(receiver_id=request.user.id)
		serializer = NotificationSerializer(notifications, many=True)
		return Response(serializer.data)

	def read(self, request, pk):
		notification = get_object_or_404(self.queryset, id=pk)
		notification.read = True
		notification.save()
		return Response(status=status.HTTP_200_OK)
