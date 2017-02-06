from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models

from ..accounts.models import Account, Group
from ..classrooms.models import Classroom


class Task(models.Model):
	CLASS, HOMEWORK, QUIZ, EXAM, TODO, GROUP_MEETING = 0, 1, 2, 3, 4, 5
	EVENT, TASK = 0, 1

	CATEGORY_CHOICES = (
		(CLASS, 'Class'),
		(HOMEWORK, 'Homework'),  # due_date, repeat
		(QUIZ, 'Quiz'),  # assigned to class or only due_date, repeat
		(EXAM, 'Exam'),  # start, end
		(TODO, 'Todo'),  # due_date, repeat
		(GROUP_MEETING, 'Group Meeting'),  # start, end, repeat
	)

	TYPE_CHOICES = (
		(EVENT, 'Event'),
		(TASK, 'Task')
	)

	# Details
	task_name = models.CharField(max_length=50)
	description = models.CharField(max_length=500, null=True, blank=True)  # task_description
	category = models.IntegerField(default=TASK, choices=CATEGORY_CHOICES)
	type = models.IntegerField(default=TASK, choices=TYPE_CHOICES)
	location = models.CharField(max_length=50, null=True, blank=True)

	# Time
	start = models.DateTimeField(blank=True, null=True)
	end = models.DateTimeField(blank=True, null=True) # the end equals to due
	# due = models.DateTimeField(blank=True, null=True)
	repeat = models.CharField(max_length=20, default='')  # MoTuWeThFi
	repeat_start = models.DateField(null=True)
	repeat_end = models.DateField(null=True)

	# Relationship
	involved = models.ManyToManyField(Account, related_name='tasks', blank=True)
	finished = models.ManyToManyField(Account, related_name='finished_tasks', blank=True)
	classroom = models.ForeignKey(Classroom, blank=True, null=True, related_name='tasks', on_delete=models.CASCADE)
	group = models.ForeignKey(Group, blank=True, null=True, related_name='tasks', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.task_name

	@property
	def expired(self):
		if self.end:
			print timezone.now(), self.end
			return timezone.now() - timedelta(hours=5) > self.end
		if self.repeat_end:
			return timezone.now() - timedelta(hours=5) > self.repeat_end

	@property
	def formatted_start_datetime(self):
		return self.start.strftime('%Y-%m-%dT%H:%M:%S')

	@property
	def formatted_end_datetime(self):
		return self.end.strftime('%Y-%m-%dT%H:%M:%S')

	@property
	def formatted_start_date(self):
		return self.start.strftime('%Y-%m-%d')

	@property
	def formatted_end_date(self):
		return self.end.strftime('%Y-%m-%d')

	@property
	def formatted_start_time(self):
		return self.start.strftime('%H:%M:%S')

	@property
	def formatted_end_time(self):
		return self.end.strftime('%H:%M:%S')


	@property
	def repeat_list(self):
		repeat_list = []
		if 'Mo' in self.repeat:
			repeat_list.append(1)
		if 'Tu' in self.repeat:
			repeat_list.append(2)
		if 'We' in self.repeat:
			repeat_list.append(3)
		if 'Th' in self.repeat:
			repeat_list.append(4)
		if 'Fr' in self.repeat:
			repeat_list.append(5)
		if 'Sa' in self.repeat:
			repeat_list.append(6)
		if 'Su' in self.repeat:
			repeat_list.append(7)

		return repeat_list
