from django.db import models

from ..accounts.models import Account

class Major(models.Model):
	major_short = models.CharField(max_length=10)
	major_full = models.CharField(max_length=100)
	major_college = models.CharField(max_length=100)

	def __unicode__(self):
		return self.major_short

class Semester(models.Model):
	name = models.CharField(max_length=20)
	start = models.DateField(null=True, blank=True)
	end = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.name


class Classroom(models.Model):
	# Basic
	class_name = models.CharField(max_length=100)
	class_number = models.CharField(max_length=10)
	class_code = models.CharField(max_length=10, unique=True)
	class_section = models.CharField(max_length=10)
	class_credit = models.CharField(max_length=10, default='3')
	class_room = models.CharField(max_length=50)
	syllabus = models.FileField(blank=True, null=True)
	description = models.TextField(blank=True)
	class_time = models.ForeignKey('tasks.Task', related_name='classtime',blank =True)
	# start = models.TimeField(blank=True, null=True)
	# end = models.TimeField(blank=True, null=True)
	# repeat = models.CharField(max_length=10, blank=True, null=True)  # MoTuWeThFi
	# Timestamp
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Relations
	professor = models.ManyToManyField(Account, related_name='teaches', blank=True)
	chatroom = models.ForeignKey('chat.Room', related_name='classroom', blank=True, null=True)
	major = models.ForeignKey(Major)
	students = models.ManyToManyField(Account, related_name='classrooms', blank=True)
	semester = models.ForeignKey(Semester)
	# Relatives
	# 1) notes
	# 2) tasks
	# 3) groups
	# 4) class_chatroom

	def __unicode__(self):
		return self.major.major_short + ' ' + self.class_number

	@property
	def students_count(self):
		return len(self.students.all())

	@property
	def class_short(self):
		return self.major.major_short + ' ' + self.class_number


class Professor(models.Model):
	email = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	classrooms = models.ManyToManyField(Classroom, related_name='professors')
	major = models.ForeignKey(Major)

