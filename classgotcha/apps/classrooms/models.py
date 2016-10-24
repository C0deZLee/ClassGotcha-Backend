from django.db import models

from ..accounts.models import Account, Major


class Classroom(models.Model):
	# Basic
	class_name = models.CharField(max_length=100)
	class_number = models.IntegerField()
	class_code = models.IntegerField()
	syllabus = models.URLField(blank=True, null=True)
	description = models.TextField(blank=True)
	# Relations
	professor = models.ManyToManyField(Account, related_name='teaches', blank=True)
	major = models.ForeignKey(Major)
	students = models.ManyToManyField(Account, related_name='classrooms', blank=True)
# Groups, Tasks
