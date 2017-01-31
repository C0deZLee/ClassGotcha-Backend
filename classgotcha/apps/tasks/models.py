from django.db import models

from ..accounts.models import Account, Group
from ..classrooms.models import Classroom


class Task(models.Model):
	EVENT, TASK = 0, 1

	STATUS_CHOICES = (
		(EVENT, 'event'),
		(TASK, 'task')
		# (HOMEWORK, 'Homework'),  # due_date, repeat
		# (QUIZ, 'Quiz'),  # assigned to class or only due_date, repeat
		# (TODO, 'Todo'),  # due_date, repeat
		# (GROUP_MEETING, 'Group Meeting'),  # start, end, repeat
		# (EXAM, 'Exam'),  # start, end
		# (CLASS, 'Class'),  # start, end, repeat

	)

	task_name = models.CharField(max_length=50)
	description = models.CharField(max_length=500, null=True, blank=True)  # task_description
	start = models.DateTimeField(blank=True, null=True)
	end = models.DateTimeField(blank=True, null=True)
	due = models.DateTimeField(blank=True, null=True)
	type = models.IntegerField(default=EVENT, choices=STATUS_CHOICES)
	repeat = models.CharField(max_length=20, default='')  # MoTuWeThFi
	repeat_start = models.DateField(null=True)
	repeat_end = models.DateField(null=True)
	location = models.CharField(max_length=50, null=True)
	# Relationship
	involved = models.ManyToManyField(Account, related_name='tasks', blank=True)
	classroom = models.ForeignKey(Classroom, blank=True, null=True, related_name='tasks', on_delete=models.CASCADE)
	group = models.ForeignKey(Group, blank=True, null=True, related_name='tasks', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.task_name

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
	def formatted_due_datetime(self):
		return self.due.strftime('%Y-%m-%dT%H:%M:%S')

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
