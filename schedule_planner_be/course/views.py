from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Course, Comment, Lesson
from Teacher.models import Teacher
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .permissions import LessonPermissionsMixin
from .forms import LessonForm


class CourseListView(ListView):
    """Вывод списка курсов"""
    model = Course
    template_name = 'course/course_list.html'


class CourseDetailView(DetailView):
    """Вывод полного описания курса"""
    model = Course
    template_name = 'course/course_detail.html'
    slug_field = 'url'


class CourseCreateView(CreateView):
    """Создание нового курса"""
    model = Course
    template_name = 'course/course_form.html'
    fields = '__all__'
    success_url = "/"


class CourseUpdateView(UpdateView):
    """Изменение курса"""
    model = Course
    template_name = 'course/course_edit.html'
    fields = '__all__'
    success_url = "/"
    slug_field = 'url'


class CourseDeleteView(DeleteView):
    """Удаление курса"""
    model = Course
    template_name = 'course/course_confirm_delete.html'
    fields = '__all__'
    success_url = "/"
    slug_field = 'url'


class CommentListView(ListView):
    """Вывод списка комментариев"""
    model = Comment
    template_name = 'course/comment_list.html'


class CommentCreateView(CreateView):
    """Создание нового комментария"""
    model = Comment
    template_name = 'course/comment_form.html'
    fields = '__all__'
    success_url = "/"


class CommentDeleteView(DeleteView):
    """Удаление комментария"""
    model = Comment
    template_name = 'course/comment_confirm_delete.html'
    fields = '__all__'
    success_url = "/"
    slug_field = 'url'


class CommentUpdateView(UpdateView):
    """Изменение курса"""
    model = Comment
    template_name = 'course/comment_edit.html'
    fields = '__all__'
    success_url = "/"
    slug_field = 'url'


class CommentDetailView(DetailView):
    """Вывод полного описания курса"""
    model = Course
    template_name = 'course/comment_detail.html'


class LessonListView(LoginRequiredMixin, ListView):
    """Вывод списка занятий"""
    model = Lesson
    template_name = 'course/lesson_list.html'


class LessonMorningListView(LoginRequiredMixin, ListView):
    """Вывод утренних занятий"""
    model = Lesson
    template_name = 'course/lesson_morning_list.html'

    def get_queryset(self):
        morning_lessons = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
        queryset = Lesson.objects.all().filter(start_time__in=morning_lessons)
        return queryset


class LessonEveningListView(LoginRequiredMixin, ListView):
    """Вывод вечерних занятий"""
    model = Lesson
    template_name = 'course/lesson_evening_list.html'

    def get_queryset(self):
        evening_lessons = ["17:00", "18:00", "19:00"]
        queryset = Lesson.objects.all().filter(start_time__in=evening_lessons)
        return queryset


class LessonDetailView(LoginRequiredMixin, DetailView):
    """Вывод полного описания зантятия"""
    model = Lesson
    template_name = 'course/lesson_detail.html'


class LessonCreateView(LoginRequiredMixin, LessonPermissionsMixin, CreateView):
    """Создание нового занятия"""
    model = Lesson
    template_name = 'course/lesson_form.html'
    form_class = LessonForm
    success_url = "/courses/lesson/"


class LessonUpdateView(LoginRequiredMixin, LessonPermissionsMixin, UpdateView):
    """Изменение занятия"""
    model = Lesson
    template_name = 'course/lesson_edit.html'
    fields = '__all__'
    success_url = "/courses/lesson/"


class LessonDeleteView(LoginRequiredMixin, LessonPermissionsMixin, DeleteView):
    """Удаление занятия"""
    model = Lesson
    template_name = 'course/lesson_confirm_delete.html'
    fields = '__all__'
    success_url = "/courses/lesson/"
