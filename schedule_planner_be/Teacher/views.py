from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Teacher, TeacherProfile
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
    success_url = "/"


class TeacherUpdateView(UpdateView):
    """Изменение учителей"""
    model = Teacher
    template_name = 'Teacher/teacher_edit.html'
    fields = ['prog_language', 'image', 'age', ]
    success_url = "/"
    slug_field = 'url'


class TeacherDeleteView(DeleteView):
    """Удаление учителя"""
    model = Teacher
    template_name = 'Teacher/teacher_confirm_delete.html'
    fields = '__all__'
    success_url = "/"
    slug_field = 'url'


class ShowProfilePageView(DetailView):
    model = TeacherProfile
    template_name = 'Teacher/Teacher_profile.html'

    def get_context_data(self, *args, **kwargs):
        teacher = TeacherProfile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_teacher = get_object_or_404(TeacherProfile, id=self.kwargs['pk'])
        context['page_teacher'] = page_teacher
        return context


class CreateProfilePageView(CreateView):
    model = TeacherProfile

    template_name = 'Teacher/create_profile.html'
    fields = ['facebook', 'twitter', 'instagram']

    def form_valid(self, form):
        form.instance.teacher = self.request.teacher
        return super().form_valid(form)

    success_url = reverse_lazy('')