from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom


class Tag(models.Model):
	# Lectures, Labs, Notes, Homeworks, Quizs, Exams,
	# Basic
	content = models.CharField(max_length=200)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	# Relationship
	# 1) Professor
	# 2) Note

	def __unicode__(self):
		return self.content

	# @property
	# def freq(self):
	# 	return self.professor.all().
