from django.db import models

from ..accounts.model import Account
from ..classrooms.model import Classroom


class Note(models.Model):
	# Relations
	creator = models.ForeignKey(Account)
	classroom = models.ForeignKey(Classroom)
	# Basics
	file = models.URLField()
	rating = models.IntegerField(null=True, blank=True)
