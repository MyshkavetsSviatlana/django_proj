import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Teacher
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeacherForm
from .permissions import TeacherPermissionsMixin


class TeacherListView(LoginRequiredMixin, ListView):
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
