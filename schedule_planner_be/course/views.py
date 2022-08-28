from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseForm
from .models import Course, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import csv
from django.http import HttpResponse

from .permissions import CoursePermissionsMixin


class CourseListView(LoginRequiredMixin, ListView):
    """Вывод списка курсов"""
    model = Course
    template_name = 'course/course_list.html'


class CourseDetailView(LoginRequiredMixin, CoursePermissionsMixin, DetailView):
    """Вывод полного описания курса"""
    model = Course
    template_name = 'course/course_detail.html'
    slug_field = 'url'


class CourseCreateView(LoginRequiredMixin, CoursePermissionsMixin, CreateView):
    # class CourseCreateView(GroupRequiredMixin, CreateView):
    """Создание нового курса"""
    group_required = u"Super Admin"
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm
    # success_url = '/courses/'


class CourseUpdateView(LoginRequiredMixin, CoursePermissionsMixin, UpdateView):
    """Изменение курса"""
    model = Course
    template_name = 'course/course_edit.html'
    fields = '__all__'
    success_url = '/courses/'
    slug_field = 'url'


class CourseDeleteView(LoginRequiredMixin, CoursePermissionsMixin, DeleteView):
    """Удаление курса"""
    model = Course
    template_name = 'course/course_confirm_delete.html'
    fields = '__all__'
    success_url = '/courses/'
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
    slug_field = 'url'


def csv_courses_list_write(request):
    """""Create a CSV file with teachers list"""
    # Get all data from Teacher Database Table
    courses = Course.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courses_list.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response, delimiter=';', dialect='excel')
    writer.writerow(['id', 'Название курса', 'Преподаватель', 'Дата начала курса', 'Кол-во занятий'])

    for course in courses:
        writer.writerow([course.id, course.course_name, course.teacher, course.start_date, course.number_of_lessons])

    return response
