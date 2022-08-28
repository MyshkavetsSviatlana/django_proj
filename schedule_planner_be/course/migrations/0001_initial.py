# Generated by Django 4.1 on 2022-08-24 12:19

import django.core.validators
from django.db import migrations, models
import django.utils.datetime_safe
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
                ('start_date', models.DateField(default=django.utils.datetime_safe.date.today, verbose_name='Course start date')),
                ('start_day_of_week', models.CharField(blank=True, default=' ', help_text='The column will be filled in automatically after saving', max_length=200, verbose_name='Start day of week')),
                ('days_of_week', multiselectfield.db.fields.MultiSelectField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=models.CharField(blank=True, default=' ', help_text='The column will be filled in automatically after saving', max_length=200, verbose_name='Start day of week'), max_length=63, verbose_name='Days of the week')),
                ('choices', models.CharField(blank=True, default=' ', max_length=200, verbose_name='Start time options')),
                ('start_time', models.CharField(choices=[('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00')], max_length=9, verbose_name='Start time')),
                ('number_of_lessons', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Number of lessons')),
                ('course_type', models.CharField(blank=True, default=' ', help_text='The column will be filled in automatically after saving', max_length=16, verbose_name='Course type')),
                ('all_course_dates', models.CharField(blank=True, default=' ', help_text='The column will be filled in automatically after saving', max_length=200, verbose_name='All course days')),
                ('url', models.SlugField(default=None, max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
