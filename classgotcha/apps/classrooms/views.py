# -*- coding: utf-8 -*-
import os, uuid, re, json
from django.core.files.base import File
from ..accounts.models import Major
from models import Account, Classroom ,Semester
from ..notes.serializers import Note, NoteSerializer
from ..posts.serializers import Moment, MomentSerializer
from ..tasks.serializers import Task, TaskSerializer
from ..accounts.serializers import BasicAccountSerializer
from django.shortcuts import get_object_or_404
from serializers import BasicClassroomSerializer, ClassroomSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny#, IsStaff
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

	# TODO search course to enroll, need to test 1/19/20217 Simo
	def search(self, request):
		try:
			search_token = request.data['search_token']
			search_token = search_token.strip()
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		if search_token.isdigit():
			try:
				classrooms = Classroom.objects.filter(class_code=search_token)
				serializer = ClassroomSerializer(classrooms, many=True)
				return (serializer.data)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)

		else:

			try:
				match = re.match(r"([a-z]+)([0-9]+)", 'foofo21', re.I)
				if match:
					items = match.groups()
				classname = items[0]
				classnumber = items[1]
				classname.upper()
				classrooms = Classroom.objects.filter(class_name=classname, class_number=classnumber)
				serializer = ClassroomSerializer(classrooms, many=True)
				return (serializer.data)

			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)


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

	# TODO
	# Tools for upload all the courses
	#@permission_classes((IsStaff,))

	def admin_upload_all_course_info(self,request,file_name = None):
		try:
			upload = request.FILES['file']
		except:
			return None
		name, extension = os.path.splitext(upload.name)

		if file_name:
			name = file_name
		name = name + '_' + uuid.uuid4().hex + extension
		
		for course in upload:
			
			cours = json.loads(course)
			print cours['description']
			major,created = Major.objects.get_or_create(major_short = cours['major'])
			semester,created  = Semester.objects.get_or_create(name = "Spring 2017")
			classroom = Classroom.objects.create(class_code=cours['number'],class_name = cours['name'].split()[0],class_number= cours['name'].split()[1],description = cours['description'],section = cours['section'],major = major,semester = semester)
			classroom.save()
		return Response(status = status.HTTP_201_CREATED)

