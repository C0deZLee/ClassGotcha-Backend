from models import Account
from rest_framework import generics, permissions
from serializers import FullAccountSerializer, BaseAccountSerializer, AuthAccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Account.objects.all()
	serializer_class = FullAccountSerializer


class AccountBasic(generics.RetrieveUpdateDestroyAPIView):
	queryset = Account.objects.all()
	serializer_class = BaseAccountSerializer


class AccountCreate(generics.CreateAPIView):
	queryset = Account.objects.all()
	serializer_class = AuthAccountSerializer


class AccountMe(generics.GenericAPIView):
	serializer_class = BaseAccountSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		return Account.objects.filter(pk=self.request.user.pk)

# from rest_framework.decorators import detail_route
#
# class AccountViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#
#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#
#     @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
#     def highlight(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
