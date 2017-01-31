from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom

from django.db import models
from django.db.models import Avg

from ..accounts.models import Account
from ..classrooms.models import Classroom
from ..tags.models import Tag


def generate_filename(self, filename):
	url = "files/users/%s/%s" % (self.classroom.class_short, filename)
	return url


class Note(models.Model):
	# Basics
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	file = models.FileField(upload_to=generate_filename)

	# Relations
	creator = models.ForeignKey(Account, related_name='notes')
	classroom = models.ForeignKey(Classroom, related_name='notes')
	tags = models.ManyToManyField(Tag, related_name='notes')

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	# Relatives
	# 1) rating

	@property
	def overall_rating(self):
		return self.rating.all().aggregate(Avg('num'))['num__avg']

	def __unicode__(self):
		return self.title


class Rate(models.Model):
	# Relations
	creator = models.ForeignKey(Account)
	num = models.IntegerField()
	note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='rating')


class Moment(models.Model):
	# Basic
	content = models.CharField(max_length=200)
	images = models.FileField(upload_to=generate_filename)
	deleted = models.BooleanField(default=False)
	solved = models.NullBooleanField()
	# Relationship
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='moments', null=True, blank=True)
	flagged_users = models.ManyToManyField(Account, null=True)
	liked_users = models.ManyToManyField(Account, related_name='liked', null=True)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='moments', null=True, blank=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# Relatives
	# 1) comments

	@property
	def flagged(self):
		return self.flagged_users.all().count() >= 3

	@property
	def likes(self):
		return self.liked_users.all().count()


class Post(models.Model):
	# Basic
	title = models.CharField(max_length=100)
	content = models.TextField()
	flagged_num = models.IntegerField(default=0)

	# Relations
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# Relatives
	# 1) comments

	@property
	def flagged(self):
		if self.flagged_num >= 3:
			return True
		else:
			return False


class Comment(models.Model):
	# Basic
	content = models.CharField(max_length=200)
	# relations
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	moment = models.ForeignKey(Moment, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
