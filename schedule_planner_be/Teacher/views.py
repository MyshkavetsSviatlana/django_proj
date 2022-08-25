from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Teacher
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeacherForm
from .permissions import TeacherPermissionsMixin


class TeacherListView(LoginRequiredMixin, ListView):
    """Вывод списка учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_list.html'


class TeacherDetailView(LoginRequiredMixin, DetailView):
    """Вывод полного описания учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_detail.html'
    slug_field = 'url'


class TeacherCreateView(LoginRequiredMixin, TeacherPermissionsMixin, CreateView):
    """Создание нового учителя"""
    model = Teacher
    template_name = 'Teacher/teacher_form.html'
    form_class = TeacherForm
    success_url = "/teachers/"


class TeacherUpdateView(LoginRequiredMixin, TeacherPermissionsMixin, UpdateView):
    """Изменение учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_edit.html'
    fields = ['surname', 'name', 'specialization', 'course_name']
    success_url = "/teachers/"
    slug_field = 'url'


class TeacherDeleteView(LoginRequiredMixin, TeacherPermissionsMixin, DeleteView):
    """Удаление учителя"""
    model = Teacher
    template_name = 'Teacher/teacher_confirm_delete.html'
    fields = '__all__'
    success_url = "/teachers/"
    slug_field = 'url'
