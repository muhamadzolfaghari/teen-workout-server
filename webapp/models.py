from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.IntegerField(unique=True)
	gender = models.CharField(max_length=10)
	age_ranges = models.CharField(max_length=20)

	def __str__(self):
		return 'user {}'.format(self.user_id)