from rest_framework import generics
from .serializers import *
from Teacher.models import Teacher
from .permissions import TeacherPermissionsMixin
from rest_framework.permissions import IsAuthenticated


class TeacherListView(generics.ListAPIView):
    """Вывод списка преподавателей"""
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all()
    permission_classes = [IsAuthenticated]


class TeacherDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания преподавателя"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
    permission_classes = [IsAuthenticated & TeacherPermissionsMixin]


class TeacherCreateView(generics.CreateAPIView):
    """Добавление преподавателя"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
    permission_classes = [IsAuthenticated & TeacherPermissionsMixin]


class TeacherUpdateView(generics.UpdateAPIView):
    """Изменение преподавателя"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherUpdateSerializer
    permission_classes = [IsAuthenticated & TeacherPermissionsMixin]


class TeacherDeleteView(generics.DestroyAPIView):
    """Удаление преподавателя"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
    permission_classes = [IsAuthenticated & TeacherPermissionsMixin]