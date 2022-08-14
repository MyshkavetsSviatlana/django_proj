from django.db import models
from django.urls import reverse


class SubwayStation(models.Model):
    station = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.station


class Location(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.IntegerField(default=None)
    subway = models.ForeignKey(SubwayStation, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.building}, {self.subway}"


class Schedule(models.Model):
    course = models.ManyToManyField('course.Course', help_text="Выберите курс")
    location = models.ManyToManyField(Location, help_text="Выберите расположение")
    teacher = models.ForeignKey('Teacher.Teacher', null=True, on_delete=models.PROTECT)
    comment = models.ManyToManyField('course.Comment')

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.id)])

    def __str__(self):
        return self.course

    class Meta:
        ordering = ['course']
