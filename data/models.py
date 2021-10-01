from django.db import models

# Create your models here.


class AgeRanges(models.Model):
    id = models.IntegerField(primary_key=True)
    range = models.CharField(max_length=100)

    class Meta:
        db_table = 'age_ranges'

    def __str__(self):
        return self.range

class Accounts(models.Model):
    id = models.IntegerField(primary_key=True)
    is_compelete = models.BooleanField()

    class Meta:
        db_table = 'accounts'


# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='userimages')
#     height = models.IntegerField(null=True)
#     weight = models.IntegerField(null=True)
#     gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, verbose_name='gender')
#     age_range_id = models.ForeignKey(AgeRanges, on_delete=models.CASCADE, null=True, verbose_name='age')
#
#     class Meta:
#         db_table = 'user'
#
#     def __str__(self):
#         return self.name


# class Gender(models.Model):
#     genders = models.CharField(max_length=30)
#
#     class Meta:
#         db_table = 'gender'
#
#     def __str__(self):
#         return self.genders
#
#
# class Food(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='foodimages')
#     measure_to_eat = models.IntegerField(null=True, verbose_name='how much?')
#
#     class Meta:
#         db_table = 'food'
#
#     def __str__(self):
#         return self.name
#
#
# class Meal(models.Model):
#     title = models.CharField(max_length=100, blank=True)
#     description = models.TextField(blank=True)
#     foods = models.ManyToManyField(Food)
#
#     class Meta:
#         db_table = 'meal'
#
#     def __str__(self):
#         return self.title
#
#
# class Workout(models.Model):
#     id = models.IntegerField(primary_key=True)
#     workout = models.CharField(max_length=100)
#     length = models.IntegerField(null=True)
#     repeat = models.IntegerField(null=True)
#     description = models.TextField()
#     age_range_id = models.ManyToManyField(AgeRanges, null=True)
#
#     class Meta:
#         db_table = 'workout'
#
#     def __str__(self):
#         return self.workout
#
#
