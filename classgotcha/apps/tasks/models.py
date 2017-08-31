from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models

from ..accounts.models import Account, Group
from ..classrooms.models import Classroom


class Task(models.Model):
	CLASS, HOMEWORK, QUIZ, EXAM, TODO, GROUP_MEETING, OTHER, OFFICE_HOUR = 0, 1, 2, 3, 4, 5, 6, 7
	EVENT, TASK = 0, 1

	CATEGORY_CHOICES = (
		(CLASS, 'Class'),
		(HOMEWORK, 'Homework'),  # due_date, repeat
		(QUIZ, 'Quiz'),  # assigned to class or only due_date, repeat
		(EXAM, 'Exam'),  # start, end
		(TODO, 'Todo'),  # due_date, repeat
		(GROUP_MEETING, 'Group Meeting'),  # start, end, repeat
		(OTHER, 'Other'),
		(OFFICE_HOUR, 'Office Hour')
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
	end = models.DateTimeField(blank=True, null=True)  # the end equals to due
	repeat = models.CharField(max_length=20, default='')  # MoTuWeThFiSaSu
	repeat_start = models.DateField(null=True)
	repeat_end = models.DateField(null=True)

	# Relationship
	involved = models.ManyToManyField(Account, related_name='tasks', blank=True)
	finished = models.ManyToManyField(Account, related_name='finished_tasks', blank=True)
	group = models.ForeignKey(Group, null=True, related_name='tasks', on_delete=models.CASCADE)
	task_of_classroom = models.ForeignKey(Classroom, related_name='tasks', on_delete=models.CASCADE, null=True)
	creator = models.ForeignKey(Account, null=True)

	# Relation
	# classroom

	def __unicode__(self):
		return self.task_name

	@property
	def expired(self):
		# TODO: FIXME! delete this in production env!!!!!!
		if self.repeat:
			return False
		if self.repeat_end:
			return timezone.now() - timedelta(hours=5) > self.repeat_end
		if self.end:
			return timezone.now() - timedelta(hours=5) > self.end

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
		return [{'Mo':1, 'Tu':2, 'We':3, 'Th':4, 'Fr':5, 'Sa':6, 'Su':7}[x] for x in [self.repeat[i:i+2] for i in range(0, len(self.repeat), 2)]]
