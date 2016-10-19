from model import Moment
from permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from serializers import MomentSerializer

from ..comments.serializers import CommentSerializer


class MomentList(generics.ListCreateAPIView):
	serializer_class = MomentSerializer
	# Permission set
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		user = self.request.user
		return Moment.objects.filter(creator=user)


class MomentDetail(generics.RetrieveAPIView):
	queryset = Moment.objects.all()
	serializer_class = CommentSerializer
	# Permission set
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
