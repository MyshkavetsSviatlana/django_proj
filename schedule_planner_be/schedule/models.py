from django.db import models

from course.models import Course, Comment


class SubwayStation(models.Model):
    """Создание модели станций метро"""
    station = models.CharField('Станция метро', max_length=50, default=None)

    def __str__(self):
        return f"Subway station {self.station}"

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'


class Location(models.Model):
    """Создание модели Локация"""
    city = models.CharField('Город', max_length=50)
    street = models.CharField('Улица', max_length=50)
    building = models.IntegerField('Номер дома', default=None)
    subway = models.ForeignKey(SubwayStation, on_delete=models.DO_NOTHING, verbose_name='Станции метро')

    def __str__(self):
        return f"{self.city}, {self.street}, {self.building}, {self.subway}"

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Schedule(models.Model):
    """Создание модели расписания"""


    title = models.TextField(default=None)
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='Курсы')
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name='Локации')
    reviews = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, verbose_name='Комментарии')
    url = models.URLField(max_length=160, unique=True, default=None)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
