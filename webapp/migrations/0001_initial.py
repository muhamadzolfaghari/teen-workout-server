# Generated by Django 3.2.7 on 2021-09-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('age_ranges', models.CharField(max_length=20)),
            ],
        ),
    ]
