from django.db import models

from ..accounts.models import Account, Major


class Semester(models.Model):
	name = models.CharField(max_length=20)
	start = models.DateField()
	end = models.DateField()

	def __unicode__(self):
		return self.name


class Classroom(models.Model):
	# Basic
	class_name = models.CharField(max_length=100)
	class_number = models.CharField(max_length=10)
	class_code = models.CharField(max_length=10, unique=True)
	syllabus = models.FileField(blank=True, null=True)
	description = models.TextField(blank=True)
	section = models.CharField(max_length=10)
	start = models.DateTimeField(blank=True, null=True)
	end = models.DateTimeField(blank=True, null=True)
	repeat = models.CharField(max_length=10)  # MoTuWeThFi

	updated = models.DateTimeField(auto_now=True)
	# Relations
	professor = models.ManyToManyField(Account, related_name='teaches', blank=True)
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


