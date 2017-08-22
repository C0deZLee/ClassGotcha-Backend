# -*- coding: utf-8 -*-
import uuid, re, json, datetime
from django.core.files.base import File
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import parser_classes

from models import Account, Classroom, Semester, Major, Professor
from ..chatrooms.models import Chatroom

from serializers import ClassroomSerializer, MajorSerializer, OfficeHourSerializer
from ..posts.serializers import MomentSerializer, Note, NoteSerializer, Moment
from ..tasks.serializers import Task, TaskSerializer, BasicTaskSerializer, CreateTaskSerializer
from ..accounts.serializers import BasicClassroomSerializer, BasicAccountSerializer
from ..tags.serializers import ClassFolderSerializer, Tag

from ..chatrooms.matrix.matrix_api import MatrixApi


def read_file(request, file_name=None):
	uploaded_file = request.FILES.get('file', False)
	if not uploaded_file:
		return None
	name, extension = uploaded_file.name.split('.')

	if file_name:
		name = file_name
	name = name + '_' + uuid.uuid4().hex + extension
	new_file = File(file=uploaded_file, name=name)  # there you go

	return new_file


class ClassroomViewSet(viewsets.ViewSet):
	queryset = Classroom.objects.all()
	permission_classes = (IsAuthenticated,)

	'''Can pass a filename as optional variable'''

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

	@staticmethod
	def search(request):
		search_token = request.data.get('search', False)
		if not search_token:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		# only class code
		if search_token.isdigit():
			classrooms = Classroom.objects.filter(class_code=search_token)
			serializer = ClassroomSerializer(classrooms, many=True)
			return Response(serializer.data)
		# major + class number
		else:
			match = re.match(r"([a-z]+) *([0-9a-z]*)", search_token, re.I)
			if match:
				items = match.groups()
				print items
				class_major = items[0].upper()
				class_number = items[1]
				major = Major.objects.get(major_short=class_major)
				classrooms = Classroom.objects.filter(major=major,
				                                      class_number=class_number) if class_number else Classroom.objects.filter(
					major=major)
				serializer = BasicClassroomSerializer(classrooms, many=True)
				return Response(serializer.data)
			else:
				# TODO STEVE: need to consider more circumstances
				return Response({})

	def validate(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		if request.user in classroom.students:
			return Response(status=status.HTTP_200_OK)
		else:
			return Response({'error': 'You are not in this classroom'}, status=status.HTTP_403_FORBIDDEN)

	@parser_classes((MultiPartParser, FormParser,))
	def syllabus(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		new_file = read_file(request, file_name=classroom.class_code)
		if not new_file:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		classroom.syllabus = new_file
		classroom.save()
		return Response(status=status.HTTP_200_OK)

	@parser_classes((MultiPartParser, FormParser,))
	def notes(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		if request.method == 'GET':
			serializer = NoteSerializer(classroom.notes, many=True)
			return Response(serializer.data)

		elif request.method == 'POST':
			title = request.data.get('title', '')
			uploaded_file = read_file(request, file_name=title)
			raw_tags = request.data.get('tags')
			description = request.data.get('description', '')
			print request.data
			if not (uploaded_file and raw_tags and title):
				return Response(status=status.HTTP_400_BAD_REQUEST)

			new_note = Note.objects.create(file=uploaded_file,
			                               title=title,
			                               description=description,
			                               creator=request.user,
			                               classroom_id=classroom.pk)
			# Load all tags from string
			for counter, tag_name in enumerate(json.loads(raw_tags)):
				tag, created = Tag.objects.get_or_create(name=tag_name, is_for=1)  # For Note
				# The first tag is "Note", "Lecture", etc, so we use first tag as classroom folders
				if counter is 0:
					classroom.folders.add(tag)
				new_note.tags.add(tag)
			Moment.objects.create(
				content='I uploaded a new note \"' + title + '\" to the classroom, check it out!',
				creator=request.user,
				classroom=classroom)

			return Response(status=status.HTTP_201_CREATED)

	def moments(self, request, pk, page=None):
		# If no page provided, default is 1
		if not page:
			page = 1

		classroom = get_object_or_404(self.queryset, pk=pk)
		# 20 moments per page
		moments = classroom.moments.filter(deleted=False).order_by('-created')[0:int(page)*20]
		serializer = MomentSerializer(moments, many=True)
		return Response(serializer.data)

	def tasks(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		if request.method == 'GET':
			# get all not expired tasks
			# tasks = [obj for obj in  if not obj.expired]
			serializer = BasicTaskSerializer(classroom.tasks.all().order_by('end'), many=True)
			return Response(serializer.data)
		elif request.method == 'POST':
			start = request.data.get('start', None)
			end = request.data.get('end', None)
			if start and end:
				request.data['type'] = 0  # event
			elif not start and end:
				del request.data['start']
				request.data['type'] = 1  # task
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			# request.data['classroom'] = {'classroom_id': classroom.id}
			serializer = CreateTaskSerializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			serializer.save()

			Moment.objects.create(
				content='I just added a new task \"' +
				        request.data.get('task_name', '') + '\" to the classroom, check it out!',
				creator=request.user,
				classroom=classroom)

			return Response(status=status.HTTP_201_CREATED)

	def students(self, request, pk):
		classroom = get_object_or_404(self.queryset, pk=pk)
		serializer = BasicAccountSerializer(classroom.students, many=True)
		return Response(serializer.data)

	def folders(self, request, pk):
		if request.method == 'GET':
			classroom = get_object_or_404(self.queryset, pk=pk)
			folders = classroom.folders.all()
			serializer = ClassFolderSerializer(folders, many=True)
			return Response(serializer.data)
		elif request.method == 'POST':
			# TODO: for lecture and homework, no children needed,
			# for notes, we need a subclass,
			content = request.data.get('content')
			parent = request.data.get('parent')
			if content:
				Tag.objects.get(content=content)

			pass

	def office_hours(self, request, pk):
		if request.method == 'GET':
			classroom = get_object_or_404(self.queryset, pk=pk)
			return Response(OfficeHourSerializer(classroom.office_hours).data)
		elif request.method == 'POST':
			# TODO
			pass

	# Tools for upload all the courses
	@staticmethod
	def upload_all_course_info(request):
		if not request.user.is_superuser:
			return Response(status=status.HTTP_403_FORBIDDEN)

		upload = request.FILES.get('file', False)
		temp_file = open(upload.temporary_file_path())
		if upload:
			course = json.load(temp_file)
			for key, cours in course.iteritems():
				# print cours['description']
				major, created = Major.objects.get_or_create(major_short=cours['major'])
				semester, created = Semester.objects.get_or_create(name="Spring 2017")
				try:
					# create class time
					time = Task.objects.create(task_name=cours['name'] + ' - ' + cours['section'],
					                           location=cours['room'],
					                           type=0,  # Event
					                           category=0  # Class
					                           )
					class_time = cours['time'].split()
					if len(class_time) == 4:
						time.repeat = class_time[0]
						time.start = datetime.datetime.strptime(class_time[1], '%I:%M%p')
						time.end = datetime.datetime.strptime(class_time[3], '%I:%M%p')
						time.save()
						print time.start, time.end, class_time[1], class_time[3]
					# create classroom
					classroom, created = Classroom.objects.get_or_create(class_code=cours['number'],
					                                                     class_number=cours['name'].split()[1],
					                                                     class_name=cours['fullName'],
					                                                     description=cours['description'],
					                                                     class_section=cours['section'],
					                                                     class_credit=cours['unit'],
					                                                     class_location=cours['room'],
					                                                     class_time=time,
					                                                     major=major,
					                                                     semester=semester)
					# create professor
					if 'instructor1' in cours:
						if 'instructor1_email' in cours:
							instructor1, created = Professor.objects.get_or_create(
								first_name=cours['instructor1'].split()[0],
								last_name=cours['instructor1'].split()[1],
								major=major, email=cours['instructor1_email'])
						else:
							instructor1, created = Professor.objects.get_or_create(
								first_name=cours['instructor1'].split()[0],
								last_name=cours['instructor1'].split()[1],
								major=major)
						classroom.professors.add(instructor1)

					if 'instructor2' in cours:
						if 'instructor2_email' in cours:
							instructor2, created = Professor.objects.get_or_create(
								first_name=cours['instructor2'].split()[0],
								last_name=cours['instructor2'].split()[1],
								major=major, email=cours['instructor2_email'])
						else:
							instructor2, created = Professor.objects.get_or_create(
								first_name=cours['instructor2'].split()[0],
								last_name=cours['instructor2'].split()[1],
								major=major)
						classroom.professors.add(instructor2)

					# save classroom to get pk in db
					classroom.save()

					# create chatrooms
					# matrix = MatrixApi(auth_token=request.user.matrix_token)
					# matrix_id = matrix.create_room(name=cours['name'] + ' - ' + cours['section'] + ' Chat Room')['room_id']

					# Chatroom.objects.create(creator=Account.objects.get(is_superuser=True),
					#                         room_type="Classroom",
					#                         # matrix_id=matrix_id,
					#                         name=cours['name'] + ' - ' + cours['section'] + ' Chat Room',
					#                         classroom=classroom)
				except IntegrityError:
					print IntegrityError
			return Response(status=status.HTTP_201_CREATED)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)


class MajorViewSet(viewsets.ViewSet):
	queryset = Major.objects.all().order_by('major_short')
	permission_classes = (IsAuthenticated,)

	def list(self, request):
		serializer = MajorSerializer(self.queryset, many=True)
		return Response(serializer.data)
