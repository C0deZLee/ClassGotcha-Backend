from __future__ import unicode_literals

from django.db import models
from ..accounts.models import Account
from ..classrooms.models import Classroom


class Room(models.Model):
	name = models.CharField(max_length=20)
	room_id = models.CharField(max_length=200)
	room_alias = models.CharField(max_length=200)

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	accounts = models.ManyToManyField(Account,related_name = 'chatrooms',null = True)
	room_type = models.CharField(max_length=200) # type = Classroom/Private/one on one
	classroom = models.ManyToManyField(Classroom, related_name = 'chatroom', null= True) 

	class Meta:
		ordering = ("name",)

	def __unicode__(self):
		return self.name
