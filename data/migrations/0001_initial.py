# Generated by Django 3.2.7 on 2021-10-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRanges',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('range', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'age_ranges',
            },
        ),
    ]
