from models import Account
from models import Classroom
from rest_framework import generics
from serializers import BasicClassroomSerializer


class ClassroomList(generics.ListCreateAPIView):
	queryset = Account.objects.all()
	serializer_class = BasicClassroomSerializer


class MyClassrooms(generics.ListCreateAPIView):
	serializer_class = BasicClassroomSerializer

	def get_queryset(self):
		return Classroom.objects.filter(students_id=self.request.user.pk)
