from rest_framework import viewsets
from api.location.serializers import LocationSerializer
from schedule.models import Location


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


