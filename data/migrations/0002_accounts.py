# Generated by Django 3.2.7 on 2021-10-01 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_compelete', models.BooleanField()),
            ],
        ),
    ]