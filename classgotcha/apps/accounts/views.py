from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from model import Account
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from serializers import AccountSerializer


class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def accounts_list(request):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		account = Account.objects.all()
		serializer = AccountSerializer(account, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = AccountSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def accounts_detail(request, pk):
	"""
	Retrieve, update or delete a code snippet.
	"""
	try:
		account = Account.objects.get(pk=pk)
	except Account.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = AccountSerializer(account)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = AccountSerializer(account, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		account.delete()
		return HttpResponse(status=204)
