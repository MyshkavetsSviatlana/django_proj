from django.db import models
from django.urls import reverse
from course.models import Course, Comment


class SubwayStation(models.Model):
    """Creates model Subway station"""
    station = models.CharField('Subway station', max_length=50, default=None)

    def __str__(self):
        return f"с/м {self.station}"


class Location(models.Model):
    """"Creates model Location"""
    city = models.CharField('City', max_length=50)
    street = models.CharField('Street', max_length=50)
    building = models.CharField('Building', max_length=10, default=None)
    subway = models.ForeignKey(SubwayStation, on_delete=models.DO_NOTHING, verbose_name='Станции метро')

    def __str__(self):
        return f"{self.street}, {self.building}, {self.subway}, {self.city}"


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
    """Создание модели Расписание"""

    title = models.TextField(default=None)
    lesson_date = models.CharField(max_length=10, default=" ")
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='Курсы')
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name='Локации')
    url = models.URLField(max_length=160, unique=True, default=None)

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.courses}"
