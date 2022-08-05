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
    teacher = models.ForeignKey("teachers.full_name", on_delete=models.CASCADE)
    start_day = models.DateField(default=date.today)
    DAY_OF_WEEK = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]
    day_of_week = models.CharField(
        choices=DAY_OF_WEEK,
        default=None,
    )
    time = models.TimeField(default=timezone.now)
    location = models.ForeignKey("locations.address", on_delete=models.CASCADE)
    classroom = models.ForeignKey("locations.classroom", on_delete=models.CASCADE)
    number_of_lessons = models.IntegerField(validators=[validate_number_of_lessons])
    COURSE_TYPE = [
        (1, "Evening schedule"),
        (2, "Morning schedule"),
    ]
    course_type = models.CharField(
        choices=COURSE_TYPE,
        default=None,
    )
    second_teacher = models.BooleanField()

    def __str__(self):
        return f"{self.course_name}, {self.start_day}"
