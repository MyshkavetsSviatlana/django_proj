from django.shortcuts import render
from .models import Course
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
    fields = ['time', 'location']
    success_url = "/"
    slug_field = 'url'


class CourseDeleteView(DeleteView):
    """Удаление курса"""
    model = Course
    template_name = 'course/course_confirm_delete.html'
    fields = '__all__'
    success_url = "/"
    slug_field = 'url'
