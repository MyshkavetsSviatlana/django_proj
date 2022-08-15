from django.db import models
from course.models import Course, Comment


class SubwayStation(models.Model):
    """Creates model Subway station"""
    station = models.CharField('Subway station', max_length=50, default=None)

    def __str__(self):
        return f"станция метро {self.station}"

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'


class Location(models.Model):
    """"Creates model Location"""
    city = models.CharField('City', max_length=50)
    street = models.CharField('Street', max_length=50)
    building = models.CharField('Building', max_length=10, default=None)
    subway = models.ForeignKey(SubwayStation, on_delete=models.DO_NOTHING, verbose_name='Станции метро')

    def __str__(self):
        return f"{self.street}, {self.building}, {self.subway}, {self.city}"

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Classroom(models.Model):
    """Creates model Classroom"""
    classroom = models.CharField('Classroom', max_length=10)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    seats_number = models.PositiveSmallIntegerField("Number of seats")
    pc_number = models.PositiveSmallIntegerField("Number of PCs")

    def __str__(self):
        return f"ауд. {self.classroom}, {self.location}"

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        unique_together = ('classroom', 'location')


class Schedule(models.Model):
    """Creates model Schedule"""

    title = models.TextField(default=None)
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='Курсы')
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name='Локации')
    reviews = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, verbose_name='Комментарии')
    url = models.URLField(max_length=160, unique=True, default=None)

    def __str__(self):
        return f'{self.courses}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
