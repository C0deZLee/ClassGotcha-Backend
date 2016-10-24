from django.db import models

from ..accounts.models import Account


class Comment(models.Model):
	# Basic
	content = models.CharField(max_length=200)
	image = models.URLField(blank=True, null=True)
	# relations
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	# how related_name work:
	# http://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
	# note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
# related names
