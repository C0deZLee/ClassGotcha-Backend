from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom
from ..groups.models import Group


class Task(models.Model):
	HOMEWORK, GROUP_MEETING, EXAM, QUIZ, TODO = 0, 1, 2, 3, 4

	STATUS_CHOICES = (
		(HOMEWORK, 'Homework'),
		(GROUP_MEETING, 'Group Meeting'),
		(EXAM, 'Exam'),
		(QUIZ, 'Quiz'),
		(TODO, 'Todo'),
	)

	task_name = models.CharField(max_length=50)
	task_des = models.CharField(max_length=500, blank=True) #task_description
	start = models.DateTimeField(blank=True, null=True)
	end = models.DateTimeField(blank=True, null=True)
	due_date = models.DateTimeField(blank=True, null=True)
	type = models.IntegerField(default=HOMEWORK, choices=STATUS_CHOICES)
	# Relationship
	involved = models.ManyToManyField(Account, related_name='tasks', blank=True, null=True)
	classroom = models.ForeignKey(Classroom, blank=True, null=True, related_name='tasks')
	group = models.ForeignKey(Group, blank=True, null=True)

	def __unicode__(self):
		return self.task_name

