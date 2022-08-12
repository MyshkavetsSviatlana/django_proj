from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import date
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError

from Teacher.models import Teacher
from User.models import User



def validate_start_day(value):
    todaydate = date.today()
    if value < todaydate:
        raise ValidationError(
            'Start day is in the past',
            params={'value': value},
        )


class Course(models.Model):
    """Создание модели Course"""
    course_name = models.CharField("Course name", max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    start_day = models.DateField("Course start day", default=date.today, validators=[validate_start_day])
    DAYS_OF_WEEK = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    )
    days_of_week = MultiSelectField("Days of the week", choices=DAYS_OF_WEEK, max_choices=7,
                                    max_length=63, default=None)
    start_time = models.TimeField("Start ime", default=timezone.now)
    end_time = models.TimeField("End time", default=timezone.now)
    location = models.ForeignKey("schedule.Classroom", on_delete=models.DO_NOTHING)
    number_of_lessons = models.PositiveSmallIntegerField("Number of lessons", default=0)
    COURSE_TYPE = [
        ("Evening schedule", "Evening schedule"),
        ("Morning schedule", "Morning schedule"),
    ]
    course_type = models.CharField("Course type",
                                   choices=COURSE_TYPE,
                                   default=None,
                                   max_length=50,
                                   )

    url = models.URLField(max_length=160, unique=True, default=None)

    def __str__(self):
        return f"{self.course_name}, {self.start_day}"

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Comment(models.Model):
    """Создание модели Комментарий"""
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.body}'
