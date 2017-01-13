import os

from django.core.files.base import File

from models import Account, Classroom
from ..notes.models import Note
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

	@parser_classes((MultiPartParser, FormParser,))
	def syllabus(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		try:
			upload = request.FILES['file']
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		filename, file_extension = os.path.splitext(upload.name)
		# filename = str(request.user.id) + file_extension
		with open(filename, 'wb+') as temp_file:
			for chunk in upload.chunks():
				temp_file.write(chunk)
		syllabus = open(filename)
		new_file = File(file=syllabus)  # there you go

		classroom.syllabus = new_file
		classroom.save()
		return Response(status=status.HTTP_200_OK)

	@parser_classes((MultiPartParser, FormParser,))
	def notes(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		try:
			upload = request.FILES['file']
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		filename, file_extension = os.path.splitext(upload.name)
		# filename = str(request.user.id) + file_extension
		with open(filename, 'wb+') as temp_file:
			for chunk in upload.chunks():
				temp_file.write(chunk)
		syllabus = open(filename)
		new_file = File(file=syllabus)  # there you go
		new_note = Note(file=new_file)
		new_note.creator = request.user
		new_note.classroom = classroom
		new_note.save()
		return Response(status=status.HTTP_201_CREATED)

	def recent_moments(self, request, pk):
		pass

	def task(self, request, pk):
		pass
