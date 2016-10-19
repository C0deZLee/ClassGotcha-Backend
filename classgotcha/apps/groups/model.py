from django.db import models
from ..accounts.model import Account
from ..classrooms.model import Classroom


class Group(models.Model):
	# Basic Info
	group_type = models.TextField()
	# Relations
	members = models.ManyToManyField(Account, blank=True)
	classroom = models.ForeignKey(Classroom, blank=True, null=True)
	creator = models.ForeignKey(Account, related_name='created_groups')

	# events = models.ForeignKey(Tasks)
