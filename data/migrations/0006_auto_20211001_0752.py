# Generated by Django 3.2.7 on 2021-10-01 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20211001_0745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='is_compeleted',
            new_name='is_completed',
        ),
        migrations.RenameField(
            model_name='accountsprofiles',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='accountsprofiles',
            old_name='age_range_id',
            new_name='age_range',
        ),
    ]
