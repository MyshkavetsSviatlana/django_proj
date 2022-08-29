from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .serializers import *
from course.models import Lesson
from .permissions import LessonPermissionsMixin
from rest_framework.permissions import IsAuthenticated
from .service import LessonFilter, LessonTeacherFilter


class LessonListView(generics.ListAPIView):
    """Вывод списка занятий"""
    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LessonTeacherFilter
    queryset = Lesson.objects.all()


class LessonMorningListView(generics.ListAPIView):
    """Вывод утренних занятий"""
    serializer_class = LessonListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, )
    filterset_class = LessonFilter

    def get_queryset(self):
        morning_lessons = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
        lessons = Lesson.objects.all().filter(start_time__in=morning_lessons)
        return lessons


class LessonEveningListView(generics.ListAPIView):
    """Вывод вечерних занятий"""
    serializer_class = LessonListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LessonFilter

    def get_queryset(self):
        evening_lessons = ["17:00", "18:00", "19:00"]
        lessons = Lesson.objects.all().filter(start_time__in=evening_lessons)
        return lessons


class LessonDetailView(generics.RetrieveAPIView):
    """Вывод полного описания занятия"""
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated & LessonPermissionsMixin]


class LessonCreateView(generics.CreateAPIView):
    """Добавление занятия"""
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated & LessonPermissionsMixin]


class LessonUpdateView(generics.UpdateAPIView):
    """Изменение занятия"""
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated & LessonPermissionsMixin]


class LessonDeleteView(generics.DestroyAPIView):
    """Удаление занятия"""
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated & LessonPermissionsMixin]