from rest_framework import generics
from .serializers import TeacherListSerializer, TeacherDetailSerializer, TeacherCreateSerializer
from Teacher.models import Teacher


class TeacherListView(generics.ListAPIView):
    """Вывод списка преподавателей"""
    serializer_class = TeacherListSerializer

    def get_queryset(self):
        users = Teacher.objects.all()
        return users


class TeacherDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания преподавателя"""
    queryset = Teacher.objects.filter()
    serializer_class = TeacherDetailSerializer


# class TeacherCreateView(generics.CreateAPIView):
#     """Добавление преподавателя"""
#     serializer_class = TeacherCreateSerializer