from django.db import models


class BadgeType(models.Model):
	TYPE_CHOICE = (
		(0, 'Note'),
		(1, 'Professor'),
		(2, 'Calendar'),
	)

	# Basic
	name = models.CharField(max_length=200, unique=True)
	type = models.IntegerField(default=0, choices=TYPE_CHOICE)

	def __unicode__(self):
		return self.name


class Badge(models.Model):
	counter = models.IntegerField(default=0)
	started = models.DateTimeField(auto_now_add=True)
	finished = models.DateTimeField(null=True, blank=True)

	# Relationship
	account = models.ForeignKey('accounts.Account', related_name='badges', on_delete=models.CASCADE)
	badge_type = models.ForeignKey(BadgeType, on_delete=models.CASCADE)

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.badge_type


class Action(models.Model):
	name = models.CharField(max_length=200, unique=True)
	exp = models.IntegerField()

	def __unicode__(self):
		return self.name
