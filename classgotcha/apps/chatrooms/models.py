from __future__ import unicode_literals

from django.db import models
from ..accounts.models import Account
from ..classrooms.models import Classroom


class Chatroom(models.Model):
	class_room, private, one_on_one = 0, 1, 2
	type_choices = (
		(class_room, 'Classroom'),
		(private, 'Private'),
		(one_on_one, 'One on One')
	)
	matrix_id = models.CharField(max_length=200)
	room_name = models.CharField(max_length=200)
	room_type = models.IntegerField(default=class_room, choices=type_choices)

	# Relations
	classroom = models.ForeignKey(Classroom, related_name='chatrooms', null=True)
	admin = models.ForeignKey(Account, related_name='created_chatrooms', null=True)
	members = models.ManyToManyField(Account, related_name='chatrooms')
	invitees = models.ManyToManyField(Account, related_name='pending_chatrooms')

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ("room_name",)

	def __unicode__(self):
		return self.name
