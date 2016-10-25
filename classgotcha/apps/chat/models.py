from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

from accounts.models import Account

class ChatRoom(models.Model):

    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True)


    class Meta:
        ordering = ("name",)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ("room", (self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ChatRoom, self).save(*args, **kwargs)


class ChatUser(models.Model):

    name = models.ForeignKey(Account,max_length=20,related_name = "name")
    session = models.CharField(max_length=20)
    room = models.ForeignKey(ChatRoom, related_name="users")

    class Meta:
        ordering = ("name",)


    def __unicode__(self):
        return self.name

