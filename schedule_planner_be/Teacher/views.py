from .models import Teacher
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class TeacherListView(ListView):
    """Вывод списка учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_list.html'


class TeacherDetailView(DetailView):
    """Вывод полного описания учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_detail.html'
    slug_field = 'url'


class TeacherCreateView(CreateView):
    """Создание нового учителя"""
    model = Teacher
    template_name = 'Teacher/teacher_form.html'
    fields = '__all__'
    success_url = "/teachers/"


class TeacherUpdateView(UpdateView):
    """Изменение учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_edit.html'
    fields = ['surname', 'name', 'specialization']
    success_url = "/teachers/"
    slug_field = 'url'


class TeacherDeleteView(DeleteView):
    """Удаление учителя"""
    model = Teacher
    template_name = 'Teacher/teacher_confirm_delete.html'
    fields = '__all__'
    success_url = "/teachers/"
    slug_field = 'url'
