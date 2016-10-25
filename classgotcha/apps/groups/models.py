from django.db import models
from ..accounts.models import Account
from ..classrooms.models import Classroom


class Group(models.Model):
	# Basic Info
	# class, subclass, individual, club
	group_type = models.CharField(max_length=20)
	# Relations
	members = models.ManyToManyField(Account, blank=True, related_name='joined_groups')
	classroom = models.ForeignKey(Classroom, blank=True, null=True, related_name='groups')
	creator = models.ForeignKey(Account, related_name='created_groups')
	# events = models.ForeignKey(Tasks)
