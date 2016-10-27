from model import Moment
from permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from serializers import MomentSerializer, CommentSerializer


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'accounts': reverse('accounts-list', request=request, format=format),
		'moments': reverse('moments-list', request=request, format=format)
	})


class MomentList(generics.ListAPIView):
	queryset = Moment.objects.all()
	serializer_class = MomentSerializer
	# Permission set
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MomentDetail(generics.RetrieveAPIView):
	queryset = Moment.objects.all()
	serializer_class = CommentSerializer
	# Permission set
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
