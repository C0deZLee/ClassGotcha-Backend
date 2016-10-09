from django.db import models

from ..accounts.model import Account
from ..classrooms.model import Classroom


class Group(models.Model):
	# Basic Info
	group_type = models.TextField()
	# Relations
	members = models.ManyToManyField(Account, blank=True, null=True)
	classroom = models.ForeignKey(Classroom, blank=True, null=True)
	# events = models.ForeignKey(Tasks)
