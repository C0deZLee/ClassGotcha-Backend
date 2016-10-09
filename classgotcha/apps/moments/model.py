from django.db import models

from ..accounts.model import Account


class Moment(models):
	# Basic
	content = models.CharField(max_length=200)
	images = models.TextField(default='[]')
	creator = models.ForeignKey(Account, on_delete=models.CASCADE)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Comments(models):
	# Basic
	content = models.CharField(max_length=200)
	images = models.TextField(default='[]')
	creator = models.ForeignKey(Account, on_delete=models.CASCADE)
	belongs_to = models.ForeignKey(Moment, on_delete=models.CASCADE)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
