from django.db import models


class SubwayStation(models.Model):
    station = models.CharField(max_length=50, default=None)


class Location(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.IntegerField(default=None)
    subway = models.ForeignKey(SubwayStation, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.building}, {self.subway}"