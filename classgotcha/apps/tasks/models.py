from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom
from ..groups.models import Group


class Task(models.Model):
	task_name = models.CharField(max_length=50)
	task_des = models.CharField(max_length=500, blank=True)
	start = models.DateTimeField(blank=True, null=True)
	end = models.DateTimeField(blank=True, null=True)
	due_date = models.DateTimeField(blank=True, null=True)
	type = models.CharField(max_length=50)  # hw, group meeting, exam
	# Relationship
	involved = models.ManyToManyField(Account)
	classroom = models.ForeignKey(Classroom, blank=True, null=True)
	group = models.ForeignKey(Group, blank=True, null=True)
