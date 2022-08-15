from rest_framework import serializers
from schedule.models import SubwayStation


class SubwayStationListSerializer(serializers.ModelSerializer):
    """Список курсов"""
    class Meta:

        model = SubwayStation
        fields = '__all__'
