from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date
from django.core.exceptions import ValidationError


def validate_number_of_lessons(value):
    """"Проверить кол-во занятий по курсу. Число должно быть натуральным."""
    if value < 0:
        raise ValidationError("Number of lessons should be more than 0")


class Course(models.Model):
    """Создание модели Course"""
    course_name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    start_day = models.DateField(default=date.today)
    DAY_OF_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    day_of_week = models.CharField(
        choices=DAY_OF_WEEK,
        default=None,
        max_length=50
    )
    time = models.TimeField(default=timezone.now)
    location = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50)
    number_of_lessons = models.IntegerField(validators=[validate_number_of_lessons])
    COURSE_TYPE = [
        ("Evening schedule", "Evening schedule"),
        ("Morning schedule", "Morning schedule"),
    ]
    course_type = models.CharField(
        choices=COURSE_TYPE,
        default=None,
        max_length=50
    )
    second_teacher = models.BooleanField()

    def __str__(self):
        return f"{self.course_name}, {self.start_day}"
