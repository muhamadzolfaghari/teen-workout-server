# Generated by Django 3.2.7 on 2021-10-02 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20211001_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'meal_types',
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
    ]