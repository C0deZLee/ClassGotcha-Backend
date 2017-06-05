from django.db import models

from ..accounts.models import Account, Professor
from ..tags.models import Tag


class Major(models.Model):
	major_short = models.CharField(max_length=10)
	major_full = models.CharField(max_length=100, blank=True)
	major_college = models.CharField(max_length=100, blank=True)
	department = models.CharField(max_length=100, blank=True)
	major_icon = models.FileField(upload_to='majors/', null=True)

	def __unicode__(self):
		return self.major_short


class Semester(models.Model):
	name = models.CharField(max_length=20)
	start = models.DateField(null=True, blank=True)
	end = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.name

	def formatted_start_date(self):
		if self.start:
			return self.start.strftime('%Y-%m-%d')
		else:
			return ''

	def formatted_end_date(self):
		if self.end:
			return self.end.strftime('%Y-%m-%d')
		else:
			return ''


class Classroom(models.Model):
	# Basic
	class_name = models.CharField(max_length=100)
	class_number = models.CharField(max_length=10)
	class_code = models.CharField(max_length=10, unique=True)
	class_section = models.CharField(max_length=10)
	class_credit = models.CharField(max_length=10, default='3')
	class_location = models.CharField(max_length=50)
	syllabus = models.FileField(upload_to='class_syllabus', blank=True, null=True)
	description = models.TextField(blank=True)
	# Timestamp
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Relations
	class_time = models.ForeignKey('tasks.Task', related_name='classtime', null=True)
	professors = models.ManyToManyField(Professor, related_name='classrooms')
	major = models.ForeignKey(Major)
	students = models.ManyToManyField(Account, related_name='classrooms')
	semester = models.ForeignKey(Semester)
	folders = models.ManyToManyField(Tag) 	# Use tag to implement folders

	# Relatives
	# 1) notes
	# 2) tasks
	# 3) groups
	# 4) chatrooms
	# 5) office_hours

	def __unicode__(self):
		return self.major.major_short + ' ' + self.class_number

	@property
	def students_count(self):
		return len(self.students.all())

	@property
	def class_short(self):
		return self.major.major_short + ' ' + self.class_number

	@property
	def class_repeat(self):
		return self.class_time.repeat

	@property
	def get_class_time(self):
		return self.class_time.start.strftime("%H:%M:%S") + self.class_time.end.strftime(" - %H:%M:%S")


class OfficeHour(models.Model):
	professor = models.ForeignKey('accounts.Professor', related_name='office_hours')
	classroom = models.ForeignKey(Classroom, related_name='office_hours')
	time = models.ForeignKey('tasks.Task', related_name='office_hour')

