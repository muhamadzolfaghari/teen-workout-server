# Generated by Django 3.2.7 on 2021-10-01 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20211001_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ageranges',
            old_name='range',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='genders',
            old_name='title',
            new_name='value',
        ),
    ]
