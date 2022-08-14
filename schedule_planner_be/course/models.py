from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date


class Course(models.Model):
    """Создание модели Course"""
    course_name = models.CharField("Название курса", max_length=50)
    teacher = models.ManyToManyField('Teacher.Teacher')
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
    day_of_week = models.CharField("День недели",
                                   choices=DAY_OF_WEEK,
                                   default=None,
                                   max_length=50
                                   )
    time = models.TimeField("Время", default=timezone.now)
    location = models.ForeignKey('schedule.Location', on_delete=models.CASCADE)
    classroom = models.CharField("Аудитория", max_length=50)
    number_of_lessons = models.PositiveSmallIntegerField("Кол-во уроков", default=0)
    COURSE_TYPE = [
        ("Evening schedule", "Evening schedule"),
        ("Morning schedule", "Morning schedule"),
    ]
    course_type = models.CharField("Вид курса",
                                   choices=COURSE_TYPE,
                                   default=None,
                                   max_length=50
                                   )
    second_teacher = models.BooleanField("Второй преподаватель")
    url = models.URLField(max_length=160, unique=True, default=None)

    def __str__(self):
        return f"{self.course_name}, {self.start_day}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    body = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.course)
