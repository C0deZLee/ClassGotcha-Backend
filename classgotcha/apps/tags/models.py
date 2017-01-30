from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom


class Tag(models.Model):
	# Basic
	content = models.CharField(max_length=200)
	# Relationship
	professors = models.ManyToManyField('accounts.Professor', related_name='tags')
	notes = models.ManyToManyField('posts.Note', related_name='tags')
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

