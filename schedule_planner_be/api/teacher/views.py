from rest_framework import generics
from .serializers import *
from Teacher.models import Teacher


class TeacherListView(generics.ListAPIView):
    """Вывод списка преподавателей"""
    serializer_class = TeacherListSerializer

    def get_queryset(self):
        teachers = Teacher.objects.all()
        return teachers


class TeacherDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания преподавателя"""
    queryset = Teacher.objects.filter()
    serializer_class = TeacherDetailSerializer


class TeacherCreateView(generics.CreateAPIView):
    """Добавление преподавателя"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer


class TeacherUpdateView(generics.UpdateAPIView):
    """Изменение преподавателя"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherUpdateSerializer


class TeacherDeleteView(generics.DestroyAPIView):
    """Удаление преподавателя"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer