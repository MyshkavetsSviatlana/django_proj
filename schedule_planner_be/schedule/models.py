from django.db import models
from django.urls import reverse
from course.models import Course, Comment


class SubwayStation(models.Model):
    """Создание модели станций метро"""
    station = models.CharField('Subway station', max_length=50, default=None)

    def __str__(self):
        return f"станция метро {self.station}"


class Location(models.Model):
    """Создание модели Локация"""
    city = models.CharField('City', max_length=50)
    street = models.CharField('Street', max_length=50)
    building = models.CharField('Building', max_length=10, default=None)
    subway = models.ForeignKey(SubwayStation, on_delete=models.DO_NOTHING, verbose_name='Станции метро')

    def __str__(self):
        return f"{self.street}, {self.building}, {self.subway}, {self.city}"


class Classroom(models.Model):
    """Создание модели Аудитория"""
    classroom = models.CharField('Classroom', max_length=10)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"аудитория {self.classroom}, {self.location}, "

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'


class Schedule(models.Model):
    """Создание модели Расписание"""
    title = models.TextField(default=None)
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='Курсы')
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name='Локации')
    reviews = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, verbose_name='Комментарии')
    url = models.URLField(max_length=160, unique=True, default=None)

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.course}"
