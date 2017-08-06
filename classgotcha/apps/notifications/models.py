from django.db import models


class Notification(models.Model):
	SYSTEM, USER = 0, 1

	FROM = (
		(SYSTEM, 'System'),
		(USER, 'User')
	)

	receiver = models.ForeignKey('accounts.Account', related_name='notifications')
	send_from = models.IntegerField(choices=FROM)
	sender = models.ForeignKey('accounts.Account', related_name='send_notifications')
	content = models.CharField(max_length=200)
	read = models.BooleanField(default=False)
	created = models.DateTimeField(auto_created=True)

	def __unicode__(self):
		return self.content
