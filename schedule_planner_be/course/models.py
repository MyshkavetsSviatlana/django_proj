import datetime
import itertools
from django.urls import reverse
from datetime import timedelta
from audioop import reverse
from django.db import models
from django.utils.datetime_safe import date
from django.core.validators import MaxValueValidator
from multiselectfield import MultiSelectField

from Teacher.models import Teacher
from User.models import User


class Course(models.Model):
    """Creates model Course"""
    # prepopulated_fields = {"course_type": ("start_time", )}
    course_name = models.CharField("Course name", max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null=True, blank=True)
    start_date = models.DateField("Course start date", default=date.today)
    start_day_of_week = models.CharField("Start day of week", max_length=200, default="", blank=True,
                                         help_text="The column will be filled in automatically after saving")

    @property
    def start_day_isoweekday(self):
        """Returns start date day of the week"""
        dw1 = self.start_date.isoweekday()
        dct = {1: "Monday",
               2: "Tuesday",
               3: "Wednesday",
               4: "Thursday",
               5: "Friday",
               6: "Saturday",
               7: "Sunday",
               }
        return dct.get(dw1)

    DAYS_OF_WEEK = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
    )
    days_of_week = MultiSelectField("Days of the week", choices=DAYS_OF_WEEK, default="",
                                    max_choices=7, max_length=63, blank=True)

    @property
    def all_course_days(self):
        """Returns all course days"""
        days_of_week = [float(item) for item in self.days_of_week]
        days_of_week_in_chosen_order = []
        for i in days_of_week:
            if i != self.start_day_isoweekday:
                days_of_week_in_chosen_order.append(int(i))
            if i == self.start_day_isoweekday:
                days_of_week_in_chosen_order.insert(0, int(i))
        all_course_days_days_of_week = []
        count = 1
        for i in itertools.cycle(days_of_week_in_chosen_order):
            if count > (self.number_of_lessons + 2):
                break
            all_course_days_days_of_week.append(i)
            count += 1
        all_course_days = []
        all_course_days.append(self.start_date)
        ind = 0
        for _ in all_course_days_days_of_week:
            if ind > self.number_of_lessons:
                break
            if all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind] > 0:
                days = all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind]
                td = timedelta(days=days)
                all_course_days.append(all_course_days[ind] + td)
            if all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind] == -1:
                days = 6
                td = timedelta(days=days)
                all_course_days.append(all_course_days[ind] + td)
            if all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind] == -2:
                days = 5
                td = timedelta(days=days)
                all_course_days.append(all_course_days[ind] + td)
            if all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind] == -3:
                days = 4
                td = timedelta(days=days)
                all_course_days.append(all_course_days[ind] + td)
            if all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind] == -4:
                days = 3
                td = timedelta(days=days)
                all_course_days.append(all_course_days[ind] + td)
            if all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind] == -5:
                days = 2
                td = timedelta(days=days)
                all_course_days.append(all_course_days[ind] + td)
            if all_course_days_days_of_week[ind + 1] - all_course_days_days_of_week[ind] == -6:
                days = 1
                td = timedelta(days=days)
                all_course_days.append(all_course_days[ind] + td)
            ind += 1
        all_course_days_str = [str(i) for i in all_course_days]
        return all_course_days_str

    @property
    def end_date(self):
        """Returns course end date"""
        end_date = self.all_course_days[-3]
        return end_date

    @property
    def transit_date_1(self):
        """Returns course transit day 1"""
        transit_date_1 = self.all_course_days[-2]
        return transit_date_1

    @property
    def transit_date_2(self):
        """Returns course transit day 1"""
        transit_date_2 = self.all_course_days[-1]
        return transit_date_2

    location = models.ForeignKey("schedule.Classroom", on_delete=models.DO_NOTHING)

    # @property
    # def loc_start_date_time(self):
    #     return str(self.location) + str(self.all_course_days) + str(self.start_time)

    START_TIME_OPTIONS = [
        ("09:00", "09:00"),
        ("10:00", "10:00"),
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

    @property
    def start_time_options(self):
        all_start_time_options = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
                                  "17:00", "18:00", "19:00"]
        all_reserved_options = [str(item) for item in
                                Course.objects.filter(start_date=self.start_date, location=self.location)]
        for a in all_reserved_options:
            for i in all_start_time_options:
                if i in a:
                    all_start_time_options.remove(i)
        # start_time_options = [(i, i) for i in all_start_time_options]
        start_time_options = [i for i in all_start_time_options]
        return start_time_options

    choices = models.CharField("Start time options", max_length=200, default="", blank=True)
    start_time = models.CharField("Start time", choices=START_TIME_OPTIONS, max_length=9)
    number_of_lessons = models.PositiveSmallIntegerField("Number of lessons", validators=[MaxValueValidator(50)])

    @property
    def find_course_type(self):
        """Returns the course type"""
        morning_course = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
        evening_course = ["17:00", "18:00", "19:00"]
        if self.start_time in morning_course:
            return "Morning schedule"
        if self.start_time in evening_course:
            return "Evening schedule"

    course_type = models.CharField("Course type", max_length=16, blank=True, default="",
                                   help_text="The column will be filled in automatically after saving")

    all_course_dates = models.CharField("All course days", max_length=200, blank=True, default="",
                                        help_text="The column will be filled in automatically after saving")

    def save(self, *args, **kwargs):
        self.start_day_of_week = self.start_date.isoweekday()
        self.course_type = self.find_course_type
        self.choices = self.start_time_options
        self.all_course_dates = self.all_course_days
        super(Course, self).save(*args, **kwargs)

    url = models.SlugField(max_length=160, unique=True, default=None)

    def __str__(self):
        return f"{self.course_name}, {self.start_date}, {self.start_time}, {self.location}"

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        unique_together = ('start_date', 'days_of_week', 'location', 'start_time')


class Comment(models.Model):
    """Creates model Comment"""
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
    body = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.body}'


class Lesson(models.Model):
    """Создание модели занятия"""
    START_TIME_OPTIONS = [
        ("09:00", "09:00"),
        ("10:00", "10:00"),
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
    number = models.PositiveSmallIntegerField("Number")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    topic = models.CharField(max_length=100)
    description = models.TextField("Description")
    date = models.DateField("Date", default=date.today)
    start_time = models.CharField("Start time", choices=START_TIME_OPTIONS, max_length=9)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"

    def __str__(self):
        return f"{self.number} {self.course} {self.topic}"
