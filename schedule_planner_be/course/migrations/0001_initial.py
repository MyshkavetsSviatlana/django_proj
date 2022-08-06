# Generated by Django 4.1 on 2022-08-05 20:18

import course.models
from django.db import migrations, models
import django.utils.datetime_safe
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
                ('start_day', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=50)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=50)),
                ('classroom', models.CharField(max_length=50)),
                ('number_of_lessons', models.IntegerField(validators=[course.models.validate_number_of_lessons])),
                ('course_type', models.CharField(choices=[('Evening schedule', 'Evening schedule'), ('Morning schedule', 'Morning schedule')], default=None, max_length=50)),
                ('second_teacher', models.BooleanField()),
            ],
        ),
    ]
