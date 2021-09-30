from django.db import models

# Create your models here.

class AgeRange(models.Model):
    id = models.IntegerField(primary_key=True)
    ages = models.CharField(max_length=100)

    class Meta:
        db_table = 'age_range'

    def __str__(self):
        return self.ages

class Gender(models.Model):
    genders = models.CharField(max_length=30)

    class Meta:
        db_table = 'gender'

    def __str__(self):
        return self.genders

class Workout(models.Model):
    id = models.IntegerField(primary_key=True)
    workout = models.CharField(max_length=100)
    length = models.IntegerField(null=True)
    repeat = models.IntegerField(null=True)
    description = models.TextField()
    age_range_id = models.ManyToManyField(AgeRange, null=True)

    class Meta:
        db_table = 'workout'

    def __str__(self):
        return self.workout

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='userimages')
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, verbose_name='gender')
    age_range_id = models.ForeignKey(AgeRange, on_delete=models.CASCADE, null=True, verbose_name='age')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name
