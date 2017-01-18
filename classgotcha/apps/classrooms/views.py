import os, uuid

from django.core.files.base import File

from models import Account, Classroom
from ..notes.serializers import Note, NoteSerializer
from ..posts.serializers import Moment, MomentSerializer
from ..tasks.serializers import Task, TaskSerializer
from ..accounts.serializers import BasicAccountSerializer
from django.shortcuts import get_object_or_404
from serializers import BasicClassroomSerializer, ClassroomSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import detail_route, list_route, api_view, permission_classes, parser_classes


class ClassroomViewSet(viewsets.ViewSet):
	queryset = Classroom.objects.all()
	permission_classes = (IsAuthenticated,)

	'''Can pass a filename as optional variable'''
	def upload(self, request, file_name=None):
		try:
			upload = request.FILES['file']
		except:
			return None
		name, extension = os.path.splitext(upload.name)

		if file_name:
			name = file_name
		name = name + '_' + uuid.uuid4().hex + extension
		with open(name, 'wb+') as temp_file:
			for chunk in upload.chunks():
				temp_file.write(chunk)
		new_file = File(file=open(name))  # there you go
		return new_file

	def retrieve(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		serializer = ClassroomSerializer(classroom)
		return Response(serializer.data)

	def update(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		for (key, value) in request.data.items():
			if key in ['description', 'syllabus']:
				setattr(classroom, key, value)
		serializer = ClassroomSerializer(classroom)
		return Response(serializer.data)

	def list(self, request):
		serializer = BasicClassroomSerializer(self.queryset, many=True)
		return Response(serializer.data)

	# TODO
	def search(self, request):
		pass

	def is_in_class(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		if request.user in classroom.students:
			return Response(status=status.HTTP_200_OK)
		else:
			return Response({'error': 'You are not in this classroom'}, status=status.HTTP_403_FORBIDDEN)

	@parser_classes((MultiPartParser, FormParser,))
	def syllabus(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		new_file = self.upload(request, file_name=classroom.class_code)
		if not new_file:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		classroom.syllabus = new_file
		classroom.save()
		return Response(status=status.HTTP_200_OK)

	@parser_classes((MultiPartParser, FormParser,))
	def notes(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		if request.method == 'POST':
			new_file = self.upload(request, file_name=classroom.class_code)
			if not new_file:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			new_note = Note(file=new_file)
			new_note.creator = request.user
			new_note.classroom = classroom
			new_note.save()
			return Response(status=status.HTTP_201_CREATED)

		if request.method == 'GET':
			serializer = NoteSerializer(classroom.notes, many=True)
			return Response(serializer.data)

	def recent_moments(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		moments = classroom.moments.all().order_by('-created')[0:5]
		serializer = MomentSerializer(moments, many=True)
		return Response(serializer.data)

	def tasks(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		if request.method == 'GET':
			serializer = TaskSerializer(classroom.tasks.all(), many=True)
			return Response(serializer.data)
		if request.method == 'POST':
			request.data['classroom'] = classroom.pk
			serializer = TaskSerializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)

	def students(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		serializer = BasicAccountSerializer(classroom.students, many=True)
		return Response(serializer.data)
