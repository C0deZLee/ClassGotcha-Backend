from django.db import models

from ..accounts.model import Account
from ..classrooms.model import Classroom


class Note(models.Model):
	# Relations
	creator = models.ForeignKey(Account)
	classroom = models.ForeignKey(Classroom)
	# Basics
	file = models.URLField()


class Rate(models.Model):
	# Relations
	creator = models.ForeignKey(Account)
	num = models.IntegerField()
	note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='rating')
