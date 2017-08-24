from django.db import models


class Action(models.Model):
	name = models.CharField(max_length=200, unique=True)
	exp = models.IntegerField()

	def __unicode__(self):
		return self.name


class BadgeType(models.Model):
	# Basic
	name = models.CharField(max_length=200, unique=True)
	action_required = models.IntegerField(default=1)
	description = models.CharField(max_length=250, blank=True, null=True)
	level = models.IntegerField(default=1)  # for example, level 1 badge for referred 1 friends, level 2 for referred 3
	identifier = models.CharField(max_length=200)

	# Relationship
	linked_actions = models.ManyToManyField(Action, related_name='linked_badge_types')

	def __unicode__(self):
		return self.name


class Badge(models.Model):
	counter = models.IntegerField(default=1)
	started = models.DateTimeField(auto_now_add=True)
	finished = models.DateTimeField(null=True, blank=True)

	# Relationship
	account = models.ForeignKey('accounts.Account', related_name='badges', on_delete=models.CASCADE)
	badge_type = models.ForeignKey(BadgeType, on_delete=models.CASCADE, related_name='type')

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.badge_type.name + '-' + self.account.email


