from django.db import models
from rest_framework import generics
from api.classroom.serializers import ClassroomListSerializer
from schedule.models import Classroom


class ClassroomListView(generics.ListAPIView):
    """Вывод списка курсов"""
    serializer_class = ClassroomListSerializer

    def get_queryset(self):
        classrooms = Classroom.objects.all()
        return classrooms


class ClassroomDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания курса"""
    queryset = Classroom.objects.filter()
    serializer_class = ClassroomListSerializer

# class CourseCreateView(generics.CreateAPIView):
#     """Добавление курса"""
#     serializer_class = CourseCreateSerializer

