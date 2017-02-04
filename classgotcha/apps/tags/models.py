from django.db import models


class Tag(models.Model):
	NOTE, PROFESSOR = 0, 1
	TYPE_CHOICE = (
		(NOTE, 'File'),
		(PROFESSOR, 'Professor'),
	)
	# Lectures, Labs, Notes, Homework, Quizzes, Exams,
	# Basic
	content = models.CharField(max_length=200, unique=True)
	type = models.IntegerField(default=NOTE, choices=TYPE_CHOICE)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	# Relationship
	# 1) Professor
	# 2) Note

	@property
	def root(self):
		return self.parent is None

	def __unicode__(self):
		return self.content


	# Default:
	# 1) Lecture
	# 2) Homework
	# 3) Lab
	# 4) Quiz
	# 5) Exam
	# 6) Note
	# 6.1) Chapter
	# 6.2) Lecture
	# 6.3) Date

	# step 1: upload file
	# step 2: choose category
	# step 2.1: choose root category
	# step 2.2: choose child category
	# step 3: upload
