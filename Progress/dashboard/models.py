from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length=200)
	college = models.CharField(max_length=200)
	about_myself = models.TextField()

	def __str__(self):
		return self.user_name