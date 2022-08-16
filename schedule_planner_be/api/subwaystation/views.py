from rest_framework import generics
from api.subwaystation.serializers import SubwayStationListSerializer
from schedule.models import SubwayStation


class SubwayStationListView(generics.ListAPIView):
    """Вывод списка станций метро"""
    serializer_class = SubwayStationListSerializer

    def get_queryset(self):
        subwaystation = SubwayStation.objects.all()
        return subwaystation


class SubwayStationDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания станции метро"""
    queryset = SubwayStation.objects.filter()
    serializer_class = SubwayStationListSerializer

# class CourseCreateView(generics.CreateAPIView):
#     """Добавление курса"""
#     serializer_class = CourseCreateSerializer

