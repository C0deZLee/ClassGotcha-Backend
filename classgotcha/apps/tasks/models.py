from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom
from ..groups.models import Group


class Task(models.Model):
	HOMEWORK, QUIZ, TODO, GROUP_MEETING, EXAM, CLASS= 0, 1, 2, 3, 4, 5

	STATUS_CHOICES = (
		(HOMEWORK, 'Homework'),
		(QUIZ, 'Quiz'),
		(TODO, 'Todo'),
		(GROUP_MEETING, 'Group Meeting'),
		(EXAM, 'Exam'),
		(CLASS,'Class'),
	)

	task_name = models.CharField(max_length=50)
	task_des = models.CharField(max_length=500, blank=True) #task_description
	start = models.DateTimeField(blank=True, null=True)
	end = models.DateTimeField(blank=True, null=True)
	due_date = models.DateTimeField(blank=True, null=True)
	type = models.IntegerField(default=HOMEWORK, choices=STATUS_CHOICES)
	repeat = models.CharField(max_length=10, blank=True, null=True)  # MoTuWeThFi
	# Relationship
	involved = models.ManyToManyField(Account, related_name='tasks')
	classroom = models.ForeignKey(Classroom, blank=True, null=True, related_name='tasks')
	group = models.ForeignKey(Group, blank=True, null=True)

	def __unicode__(self):
		return self.task_name

