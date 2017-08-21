from ..accounts.models import Account, Professor
from ..classrooms.models import Classroom

from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom
from ..tags.models import Tag

EVERYONE, STUDENTS_ONLY, PRIVATE = 0, 1, 2
PERMISSION_CHOICE = (
	(0, 'Everyone'),
	(1, 'Student_only'),
	(2, 'Private')
)


def generate_filename(self, filename):
	url = "files/users/%s/%s" % (self.classroom.class_short, filename)
	return url


class Note(models.Model):
	# Basics
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	file = models.FileField(upload_to=generate_filename)
	permission = models.IntegerField(default=EVERYONE, choices=PERMISSION_CHOICE)

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
		return self.rating.all().aggregate(models.Avg('num'))['num__avg']

	def __unicode__(self):
		return self.title


class Rate(models.Model):
	# Basic
	num = models.IntegerField()
	# Relations
	creator = models.ForeignKey(Account)
	note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='rates', null=True)
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='rates', null=True)

	# Relations
	# 1) comment

	def __unicode__(self):
		return self.num


class Moment(models.Model):
	# Basic
	content = models.CharField(max_length=200)
	images = models.FileField(upload_to=generate_filename)
	deleted = models.BooleanField(default=False)
	solved = models.NullBooleanField()
	permission = models.IntegerField(default=EVERYONE, choices=PERMISSION_CHOICE)

	# Relationship
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='moments', null=True, blank=True)
	flagged_users = models.ManyToManyField(Account)
	liked_users = models.ManyToManyField(Account, related_name='liked')
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
	TAG_CHOICES = ((0, 'Bug Report'),
	               (1, 'Suggestion'),
	               (2, 'Others'))
	# Basic
	title = models.CharField(max_length=100)
	content = models.TextField()
	flagged_num = models.IntegerField(default=0)
	permission = models.IntegerField(default=EVERYONE, choices=PERMISSION_CHOICE)
	votes = models.IntegerField(default=0)
	up_voted_user = models.ManyToManyField(Account, related_name='post_up_vote')
	down_voted_user = models.ManyToManyField(Account, related_name='post_down_vote')
	# Relations
	tag = models.IntegerField(choices=TAG_CHOICES, default=0)
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
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments', null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
	moment = models.ForeignKey(Moment, on_delete=models.CASCADE, related_name='comments', null=True)
	note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments', null=True)
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='comments', null=True)
	rate = models.OneToOneField(Rate, related_name='comment', null=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Notification(models.Model):
	content = models.TextField(max_length=200)
	user = models.ForeignKey(Account)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content
