from django.db import models

# Create your models here.

class Login(models.Model):
	family_name = models.CharField(max_length=100)
	given_name = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	user_id = models.IntegerField()
	picture = models.ImageField()
