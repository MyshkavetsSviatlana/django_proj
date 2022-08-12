# Generated by Django 4.1 on 2022-08-12 14:16

import course.models
from django.db import migrations, models
import django.utils.datetime_safe
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50, verbose_name='Course name')),
                ('start_day', models.DateField(default=django.utils.datetime_safe.date.today, validators=[course.models.validate_start_day], verbose_name='Course start day')),
                ('days_of_week', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=63, verbose_name='Days of the week')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Time')),
                ('number_of_lessons', models.PositiveSmallIntegerField(default=0, verbose_name='Number of lessons')),
                ('course_type', models.CharField(choices=[('Evening schedule', 'Evening schedule'), ('Morning schedule', 'Morning schedule')], default=None, max_length=50, verbose_name='Course type')),
                ('url', models.URLField(default=None, max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
