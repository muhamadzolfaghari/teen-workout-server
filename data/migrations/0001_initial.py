# Generated by Django 3.2.7 on 2021-10-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('image', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='AgeRanges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='age range')),
            ],
            options={
                'db_table': 'age_ranges',
            },
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='gender')),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='MealTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='meal type')),
            ],
            options={
                'db_table': 'meal_types',
            },
        ),
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='workoutsimages')),
                ('description', models.TextField()),
                ('length', models.IntegerField(null=True)),
                ('repeat', models.IntegerField(null=True)),
                ('age_range', models.ManyToManyField(to='data.AgeRanges')),
            ],
            options={
                'db_table': 'workout',
            },
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='foodsimages')),
                ('description', models.TextField()),
                ('meal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.mealtypes')),
            ],
            options={
                'db_table': 'foods',
            },
        ),
        migrations.CreateModel(
            name='DailyWorkouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('workouts', models.ManyToManyField(to='data.Workouts')),
            ],
            options={
                'db_table': 'daily_workouts',
            },
        ),
        migrations.CreateModel(
            name='AccountsProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.accounts')),
                ('age_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.ageranges')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.genders')),
            ],
            options={
                'db_table': 'accounts_profiles',
            },
        ),
    ]
