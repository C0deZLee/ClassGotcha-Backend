from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from models import Moment, Post, Comment
from serializers import MomentSerializer, PostSerializer, BasicPostSerializer

from ..notifications.models import Notification


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
		moment = get_object_or_404(self.queryset, pk=pk)
		if moment.creator_id != request.user.pk:
			return Response(status=status.HTTP_403_FORBIDDEN)
		moment.solved = True
		moment.save()
		return Response(status=status.HTTP_200_OK)

	def comment(self, request, pk):
		get_object_or_404(self.queryset, pk=pk)
		content = request.data.get('content', None)
		if content:
			Comment.objects.create(content=content, moment_id=pk, creator=request.user)
			return Response(status=status.HTTP_200_OK)
		else:
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
		if moment.creator_id is not request.user.id:
			Notification.objects.create(receiver_id=moment.creator_id, sender_id=request.user.id, content='liked your moment')
		return Response(status=status.HTTP_200_OK)


class PostViewSet(viewsets.ViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def retrieve(self, request, pk):
		post = get_object_or_404(self.queryset, pk=pk)
		serializer = PostSerializer(post)
		return Response(serializer.data)

	def list(self, request):
		posts = Post.objects.order_by('-created')
		serializer = BasicPostSerializer(posts, many=True)
		return Response(serializer.data)

	def create(self, request):
		title = request.data.get('title')
		content = request.data.get('content')
		tag = request.data.get('tag')

		if title and content and tag:
			Post.objects.create(creator_id=request.user.id, title=title, content=content, tag=tag)
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def comment(self, request, pk):
		get_object_or_404(self.queryset, pk=pk)
		content = request.data.get('content', None)
		if content:
			Comment.objects.create(content=content, post_id=pk, creator=request.user)
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def vote(self, request, pk):
		vote = request.data.get('vote')
		if vote == 1:
			post = get_object_or_404(self.queryset, pk=pk)

			if request.user not in post.down_voted_user.all() and request.user not in post.up_voted_user.all():
				post.up_voted_user.add(request.user)
				post.votes += 1
				post.save()

			return Response(status=status.HTTP_200_OK)
		elif vote == -1:
			post = get_object_or_404(self.queryset, pk=pk)

			if request.user not in post.down_voted_user.all() and request.user not in post.up_voted_user.all():
				post.down_voted_user.add(request.user)
				post.votes -= 1
				post.save()

			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
