from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import date
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
from datetime import date, timedelta

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
    """Creates model Course"""
    course_name = models.CharField("Course name", max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    start_day = models.DateField("Course start day", default=date.today, validators=[validate_start_day])

    @property
    def start_day_isoweekday(self):
        """Returns start date day of the week"""
        dw1 = self.start_day.isoweekday()
        # if dw1 == 1:
        #     return "Monday"
        # if dw1 == 2:
        #     return "Tuesday"
        # if dw1 == 3:
        #     return "Wednesday"
        # if dw1 == 4:
        #     return "Thursday"
        # if dw1 == 5:
        #     return "Friday"
        # if dw1 == 6:
        #     return "Saturday"
        # if dw1 == 7:
        #     return "Sunday"
        return int(dw1)

    DAYS_OF_WEEK = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
    )
    days_of_week = MultiSelectField("Days of the week", choices=DAYS_OF_WEEK, max_choices=7,
                                    max_length=63, default=None)

    @property
    def end_day(self):
        """Returns end date"""
        lst = [float(item) for item in self.days_of_week]
        a = max(lst) - min(lst)
        if self.number_of_lessons % 2 == 0:
            days = (self.number_of_lessons/2 - 1) * 7 + a
            td = timedelta(days=days)
            end_day = self.start_day + td
            return end_day
        if self.number_of_lessons % 2 != 0:
            days = (self.number_of_lessons//2) * 7
            td = timedelta(days=days)
            end_day = self.start_day + td
            return end_day

    @property
    def transit_day_1(self):
        """Returns transit day 1"""
        lst = [float(item) for item in self.days_of_week]
        a = max(lst) - min(lst)
        if self.number_of_lessons % 2 == 0:
            days = (self.number_of_lessons/2) * 7
            td = timedelta(days=days)
            end_day = self.start_day + td
            return end_day
        if self.number_of_lessons % 2 != 0:
            days = (self.number_of_lessons//2) * 7 + a
            td = timedelta(days=days)
            end_day = self.start_day + td
            return end_day

    @property
    def transit_day_2(self):
        """Returns transit day 2"""
        lst = [float(item) for item in self.days_of_week]
        a = max(lst) - min(lst)
        if self.number_of_lessons % 2 == 0:
            days = (self.number_of_lessons/2) * 7 + a
            td = timedelta(days=days)
            end_day = self.start_day + td
            return end_day
        if self.number_of_lessons % 2 != 0:
            days = (self.number_of_lessons//2) * 7 + 7
            td = timedelta(days=days)
            end_day = self.start_day + td
            return end_day

    location = models.ForeignKey("schedule.Classroom", on_delete=models.DO_NOTHING)

    @property
    def loc_start_day_time(self):
        return str(self.location) + str(self.start_day) + str(self.days_of_week) + str(self.start_time)

    START_TIME_OPTIONS = [
        ("09:00", "09:00"),
        ("10:00", "10:00"),
        ("10:30", "10:30"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
        ("19:00", "19:00"),
    ]
    start_time = models.CharField("Start time", choices=START_TIME_OPTIONS, default=None,
                                  max_length=5)
    # end_time = models.TimeField("End time", default=timezone.now)
    number_of_lessons = models.PositiveSmallIntegerField("Number of lessons", default=0)

    @property
    def course_type(self):
        """Returns the course type"""
        morning_course = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
        evening_course = ["17:00", "18:00", "19:00"]
        if self.start_time in morning_course:
            return "Morning schedule"
        if self.start_time in evening_course:
            return "Evening schedule"

    url = models.URLField(max_length=160, unique=True, default=None)

    def __str__(self):
        return f"{self.course_name}, {self.start_day}, {self.location}"

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.url})

    # def save(self, *args, **kwargs):
    #     if self.course_type is None:
    #         course_type = self.course_type
    #     super(Course, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        unique_together = ('start_day', 'days_of_week', 'location', 'start_time')


class Comment(models.Model):
    """Creates model Comment"""
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
