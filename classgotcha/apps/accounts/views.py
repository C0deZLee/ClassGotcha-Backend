from model import Account
from rest_framework import generics
from serializers import AccountSerializer


class AccountList(generics.ListCreateAPIView):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

#

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
