from models import Account
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import FullAccountSerializer, BaseAccountSerializer


@api_view(['POST'])
def register(request):
	serialized = BaseAccountSerializer(data=request.data)
	if serialized.is_valid():
		Account.objects.create_user(
				serialized.init_data['email'],
				serialized.init_data['username'],
				serialized.init_data['password']
		)
		return Response(serialized.data, status=status.HTTP_201_CREATED)
	else:
		return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class AccountList(generics.ListCreateAPIView):
	"""
    **GET** Get all accounts

    **POST** Create new account
	"""
	queryset = Account.objects.all()
	serializer_class = BaseAccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Account.objects.all()
	serializer_class = FullAccountSerializer


class AccountBasic(generics.RetrieveUpdateDestroyAPIView):
	queryset = Account.objects.all()
	serializer_class = BaseAccountSerializer


class AccountMe(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BaseAccountSerializer

	def get_queryset(self):
		return Account.objects.get(pk=self.request.user.pk)

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def accounts_list(request):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	if request.method == 'GET':
# 		account = Account.objects.all()
# 		serializer = AccountSerializer(account, many=True)
# 		return Response(serializer.data)
#
# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = AccountSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def accounts_detail(request, pk):
# 	"""
# 	Retrieve, update or delete a code snippet.
# 	"""
# 	try:
# 		account = Account.objects.get(pk=pk)
# 	except Account.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
# 	if request.method == 'GET':
# 		serializer = AccountSerializer(account)
# 		return Response(serializer.data)
#
# 	elif request.method == 'PUT':
# 		serializer = AccountSerializer(account, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#
# 	elif request.method == 'DELETE':
# 		account.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
