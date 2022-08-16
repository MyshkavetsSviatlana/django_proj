from django.db import models
from rest_framework import generics
from api.course.serializers import CourseListSerializer
from course.models import Course


class CourseListView(generics.ListAPIView):
    """Вывод списка курсов"""
    serializer_class = CourseListSerializer

    def get_queryset(self):
        courses = Course.objects.all()
        return courses


class CourseDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания курса"""
    queryset = Course.objects.filter()
    serializer_class = CourseListSerializer

# class CourseCreateView(generics.CreateAPIView):
#     """Добавление курса"""
#     serializer_class = CourseCreateSerializer

