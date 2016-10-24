from models import Classroom
from models import Group
from rest_framework import generics
from serializers import GroupSerializers


class GroupList(generics.ListCreateAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializers


class MyGroupsList(generics.ListCreateAPIView):
	serializer_class = GroupSerializers

	def get_queryset(self):
		return Classroom.objects.filter(students_id=self.request.user.pk)


class MyCreatedGroupList(generics.ListCreateAPIView):
	pass


class ClassGroupsList(generics.ListCreateAPIView):
	pass


class GroupMembersList(generics.ListCreateAPIView):
	pass


class GroupCreatorList(generics.ListCreateAPIView):
	pass
