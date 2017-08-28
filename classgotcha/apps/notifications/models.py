from django.db import models


class Notification(models.Model):
	receiver = models.ForeignKey('accounts.Account', related_name='notifications')
	sender = models.ForeignKey('accounts.Account', related_name='send_notifications', null=True, blank=True)
	content = models.CharField(max_length=200)
	read = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content
