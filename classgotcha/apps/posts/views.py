from models import Moment

from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from serializers import MomentSerializer, CommentSerializer, PostSerializer, Comment


class MomentViewSet(viewsets.ViewSet):
	queryset = Moment.objects.exclude(deleted=True)
	serializer_class = MomentSerializer
	# Permission set
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def retrieve(self, request, pk):
		moment = get_object_or_404(self.queryset, pk=pk)
		serializer = MomentSerializer(moment)
		return Response(serializer.data)

	def solve(self, request, pk):
		# can only change own moments' status
		if pk != request.user.pk:
			return Response(status=status.HTTP_403_FORBIDDEN)
		moment = get_object_or_404(self.queryset, pk=pk)
		moment.solved = True
		moment.save()
		return Response(status=status.HTTP_200_OK)

	def comment(self, request, pk):
		moment = get_object_or_404(self.queryset, pk=pk)
		print moment
		content = request.data.get('content', None)
		if content:
			comment = Comment(content=content, moment=moment, creator=request.user)
			comment.save()
			moment.comments.add(comment)
			moment.save()
			return Response(status=status.HTTP_200_OK)
		else:
			print "no content"
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def report(self, request, pk):
		moment = get_object_or_404(self.queryset, pk=pk)
		moment.flagged_users.add(request.user)
		if moment.flagged:
			moment.deleted = True
		moment.save()
		return Response(status=status.HTTP_200_OK)

	def like(self, request, pk):
		moment = get_object_or_404(self.queryset, pk=pk)
		moment.liked_users.add(request.user)
		moment.save()
		return Response(status=status.HTTP_200_OK)

