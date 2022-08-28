import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Teacher
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeacherForm
from .permissions import TeacherPermissionsMixin


class TeacherListView(LoginRequiredMixin, ListView):
    """Вывод списка учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_list.html'


class TeacherDetailView(LoginRequiredMixin, TeacherPermissionsMixin, DetailView):
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


def csv_teachers_list_write(request):
    """""Create a CSV file with teachers list"""
    # Get all data from Teacher Database Table
    teachers = Teacher.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="teachers_list.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response, delimiter=';', dialect='excel')
    writer.writerow(['id', 'Фамилия', 'Имя', 'Специализация', 'Телефон'])

    for teacher in teachers:
        writer.writerow([teacher.id, teacher.surname, teacher.name, teacher.specialization, teacher.phone])

    return response
