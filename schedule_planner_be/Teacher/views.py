from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Teacher
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeacherForm
from .permissions import TeacherPermissionsMixin


class TeacherListView(LoginRequiredMixin, TeacherPermissionsMixin, ListView):
    """Вывод списка учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_list.html'

    def get_queryset(self):
        teachers = Teacher.objects.filter(is_active=True)
        return teachers


class TeacherDetailView(LoginRequiredMixin, DetailView):
    """Вывод полного описания учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_detail.html'
    slug_field = 'url'

    def get_queryset(self):
        teachers = Teacher.objects.filter(is_active=True)
        return teachers


class TeacherCreateView(LoginRequiredMixin, TeacherPermissionsMixin, CreateView):
    """Создание нового учителя"""
    model = Teacher
    template_name = 'Teacher/teacher_form.html'
    form_class = TeacherForm
    success_url = "/teachers/"

    def get_queryset(self):
        teachers = Teacher.objects.filter(is_active=True)
        return teachers


class TeacherUpdateView(LoginRequiredMixin, TeacherPermissionsMixin, UpdateView):
    """Изменение учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_edit.html'
    fields = ['surname', 'name', 'specialization', 'course_name']
    success_url = "/teachers/"
    slug_field = 'url'

    def get_queryset(self):
        teachers = Teacher.objects.filter(is_active=True)
        return teachers


class TeacherDeleteView(LoginRequiredMixin, TeacherPermissionsMixin, DeleteView):
    """Изменение статуса учителя на неактивный"""
    model = Teacher
    template_name = 'Teacher/teacher_confirm_delete.html'
    fields = ['is_active']
    success_url = "/teachers/"
    slug_field = 'url'

    def get_queryset(self):
        teachers = Teacher.objects.filter(is_active=True)
        return teachers

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


