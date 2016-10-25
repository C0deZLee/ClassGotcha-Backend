from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom


class Note(models.Model):
	# Relations
	creator = models.ForeignKey(Account, related_name='notes')
	classroom = models.ForeignKey(Classroom, related_name='notes')
	# Basics
	file = models.URLField()
# Relatives
# 1) rating


class Rate(models.Model):
	# Relations
	creator = models.ForeignKey(Account)
	num = models.IntegerField()
	note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='rating')
