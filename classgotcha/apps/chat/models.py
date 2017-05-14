from __future__ import unicode_literals

from django.db import models
from ..accounts.models import Account
from ..classrooms.models import Classroom


class Room(models.Model):
	class_room ,Private,One_on_One = 0,1,2
	type_choices = (
		(class_room,'Classroom'),
		(Private,'Private'),
		(One_on_One,'One on One')  
		)
	name = models.CharField(max_length=20)
	room_id = models.CharField(max_length=200)
	room_alias = models.CharField(max_length=200)

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	accounts = models.ManyToManyField(Account,related_name = 'chatrooms',null = True)
	room_type = models.IntegerField(default=class_room,choices = type_choices) # type = Classroom/Private/one on one
	classroom = models.ManyToManyField(Classroom, related_name = 'chatroom', null= True) 




	class Meta:
		ordering = ("name",)

	def __unicode__(self):
		return self.name
