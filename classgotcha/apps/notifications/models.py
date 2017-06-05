from django.db import models


class Notification(models.Model):
	PUSHED, READ = 0, 1

	STATUS_CHOICES = (
		(PUSHED, 'Pushed'),
		(READ, 'Read')
	)

	GLOBAL, SYSTEM, USER_SIDE = 0, 1, 2

	TYPE_CHOICES = (
		(GLOBAL, 'Global'),
		(SYSTEM, 'System'),
		(USER_SIDE, 'User Side')
	)

	receiver = models.ForeignKey('accounts.Account', related_name='notifications')
	sender = models.ForeignKey('accounts.Account', related_name='send_notifications')
	content = models.CharField(max_length=200)
	status = models.IntegerField(choices=STATUS_CHOICES)
	type = models.IntegerField(choices=TYPE_CHOICES)
	created = models.DateTimeField(auto_created=True)

	def __unicode__(self):
		return self.content
