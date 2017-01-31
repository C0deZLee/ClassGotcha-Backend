from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

from ..accounts.models import Account


class Room(models.Model):
	name = models.CharField(max_length=20)
	read = models.BooleanField(default=True)

	# Relationship
	accounts = models.ManyToManyField(Account, related_name='rooms')
	creator = models.ForeignKey(Account, related_name='owned_rooms')
	classroom = models.ForeignKey('classrooms.Classroom', related_name='chatroom', on_delete=models.CASCADE, null=True)
	group = models.ForeignKey('accounts.Group', related_name='chatroom', on_delete=models.CASCADE, null=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	# Relationship
	# 1) classroom
	# 2) group
	# 3) messages

	class Meta:
		ordering = ("name",)

	def __unicode__(self):
		return self.name

	@property
	def latest_message(self):
		messages = self.messages.all()
		if messages:
			latest_message = {
				'full_name': messages[0].send_from.get_full_name,
				'message': messages[0].message,
				'created': messages[0].created.strftime('%b %-d %-I:%M %p')
			}
			return latest_message
		else:
			return {
				'full_name': '',
				'message': '',
				'created': ''
			}


class Message(models.Model):
	room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)  # send to
	context = models.CharField(max_length=140, blank=True)
	username = models.CharField(max_length=140)
	message = models.CharField(max_length=140)
	created = models.DateTimeField(auto_now_add=True, db_index=True)
	send_from = models.ForeignKey(Account, related_name='sent_messages')

	def __unicode__(self):
		return '[{created}] {username}: {message}'.format(**self.as_dict())

	@property
	def formatted_timestamp(self):
		return self.created.strftime('%b %-d %-I:%M %p')

	def as_dict(self):
		return {'send_from': self.send_from.pk,
		        'username': self.username,
		        'message': self.message,
		        'created': self.formatted_timestamp}

	class Meta:
		get_latest_by = 'created'
