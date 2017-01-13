from models import Moment

from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from serializers import MomentSerializer, CommentSerializer, PostSerializer


class MomentViewSet(viewsets.ViewSet):
	queryset = Moment.objects.exclude(flagged_num=3)
	serializer_class = MomentSerializer
	# Permission set
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def retrieve(self, request, pk):
		moment = get_object_or_404(self.queryset, pk=pk)
		serializer = MomentSerializer(moment)
		return Response(serializer.data)

	def destroy(self, request, pk):
		moment = get_object_or_404(self.queryset, pk=pk)
		moment.delete()
		return Response(status=status.HTTP_200_OK)



