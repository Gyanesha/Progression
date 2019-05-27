from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class User(models.Model):
	user_name = models.CharField(primary_key=True, max_length=200)
	college = models.CharField( max_length=200)
	score = models.IntegerField(default=0)
	about_myself = models.TextField()

	class Meta:
		managed = True
		unique_together = (('user_name', 'college'),)

	def __str__(self):
		return self.user_name