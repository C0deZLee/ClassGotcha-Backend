from time import gmtime, strftime

from django.db import models

from ..accounts.models import Account, Professor


class Major(models.Model):
	major_short = models.CharField(max_length=10)
	major_full = models.CharField(max_length=100)
	major_college = models.CharField(max_length=100)
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
	class_room = models.CharField(max_length=50)
	syllabus = models.FileField(upload_to='class_syllabus', blank=True, null=True)
	description = models.TextField(blank=True)
	# Timestamp
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Relations
	class_time = models.ForeignKey('tasks.Task', related_name='classtime', blank=True)
	professors = models.ManyToManyField(Professor, related_name='teaches', blank=True)
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

	@property
	def class_repeat(self):
		return self.class_time.repeat

	@property
	def get_class_time(self):
		return self.class_time.start.strftime("%H:%M:%S") + self.class_time.end.strftime(" - %H:%M:%S")
