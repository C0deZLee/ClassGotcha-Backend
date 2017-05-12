from django.db import models


class BadgeType(models.Model):
	NOTE, PROFESSOR, CALENDAR = 0, 1, 2
	TYPE_CHOICE = (
		(NOTE, 'File'),
		(PROFESSOR, 'Professor'),
		(CALENDAR, 'Calendar'),
	)
	# Basic
	name = models.CharField(max_length=200, unique=True)
	type = models.IntegerField(default=NOTE, choices=TYPE_CHOICE)

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	# Relationship

	def __unicode__(self):
		return self.name


class Badge(models.Model):
	badge_type = models.ForeignKey('badges.BadgeType')
	counter = models.IntegerField(default=0)
	started = models.DateTimeField(auto_now_add=True)
	finished = models.DateTimeField(null=True, blank=True)
	account = models.ForeignKey('accounts.Account')

	def __unicode__(self):
		return self.badge_type


class Action(models.Model):
	name = models.CharField(max_length=200, unique=True)
	exp = models.IntegerField()

	def __unicode__(self):
		return self.name
