from django.db import models
from django.db.models import Avg

from ..accounts.models import Account
from ..classrooms.models import Classroom


class Note(models.Model):
	# Relations
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	creator = models.ForeignKey(Account, related_name='notes')
	classroom = models.ForeignKey(Classroom, related_name='notes')
	created = models.DateTimeField(auto_now_add=True)
	# Basics
	file = models.FileField(upload_to='avatars')
	# Relatives
	# 1) rating

	@property
	def overall_rating(self):
		return self.rating.all().aggregate(Avg('num'))['num__avg']

	def __unicode__(self):
		return self.title


class Rate(models.Model):
	# Relations
	creator = models.ForeignKey(Account)
	num = models.IntegerField()
	note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='rating')
