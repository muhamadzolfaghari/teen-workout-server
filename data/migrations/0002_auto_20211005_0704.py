# Generated by Django 3.2.7 on 2021-10-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouts',
            name='length',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='repeat',
            field=models.IntegerField(null=True),
        ),
    ]
