from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

from ..accounts.models import Account


class Room(models.Model):
    name = models.CharField(max_length=20)
    # label = models.SlugField(blank=True, null=True)
    # relationship
    accounts = models.ManyToManyField(Account, related_name='rooms')
    creator = models.ForeignKey(Account, related_name='owned_rooms')
    created = models.DateTimeField(auto_now_add=True)
    # Relationship
    # 1) classroom
    # 2) group

    class Meta:
        ordering = ("name",)

    def __unicode__(self):
        return self.name

    #
    # @models.permalink
    # def get_absolute_url(self):
    # 	return ("room", (self.pk,))


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    context = models.CharField(max_length=140, blank=True)
    username = models.CharField(max_length=140)
    message = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __unicode__(self):
        return '[{created}] {username}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.created.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'username': self.username, 'message': self.message, 'created': self.formatted_timestamp}

    class Meta:
        get_latest_by = 'created'

#
# class ChatUser(models.Model):
# 	name = models.ForeignKey(Account, max_length=20, related_name="name")
# 	session = models.CharField(max_length=20)
# 	room = models.ForeignKey(Room, related_name="users")
#
# 	class Meta:
# 		ordering = ("name",)
#
# 	def __unicode__(self):
# 		return self.name
