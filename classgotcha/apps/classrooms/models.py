from django.db import models

from ..accounts.models import Account, Major


class Classroom(models.Model):
	# Basic
	class_name = models.CharField(max_length=100)
	class_number = models.CharField(max_length=10)
	class_code = models.CharField(max_length=10)
	syllabus = models.URLField(blank=True, null=True)
	description = models.TextField(blank=True)
	section = models.CharField(max_length=10)
	# Relations
	professor = models.ManyToManyField(Account, related_name='teaches', blank=True)
	major = models.ForeignKey(Major)
	students = models.ManyToManyField(Account, related_name='classrooms', blank=True)
	# Relatives
	# 1) notes
	# 2) tasks
	# 3) groups

	def __unicode__(self):
		return self.class_name + self.class_number

	@property
	def students_count(self):
		return len(self.students.all())
