from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import ScheduleForm
from .models import Location
from ..Teacher.models import Teacher
from ..course.models import Course, Comment


class ScheduleListView(ListView):
    template_name = 'schedule/schedules.html'
    model = "schedule.Schedule"


class ScheduleUpdateView(UpdateView):
    template_name = 'schedule/edit-schedule.html'
    model = "schedule.Schedule"
    form_class = ScheduleForm

    def get_success_url(self):
        return reverse_lazy('schedule-detail', args=(self.object.id,))


class ScheduleDeleteView(DeleteView):
    template_name = 'schedule/delete-schedule.html'
    model = "schedule.Schedule"
    success_url = reverse_lazy('schedules')


class ScheduleDetailView(DetailView):
    template_name = 'schedule/book-detail.html'
    model = "schedule.Schedule"


class ScheduleCreateView(CreateView):
    template_name = 'schedule/add-schedule.html'
    form_class = ScheduleForm

    def get_success_url(self):
        return reverse_lazy('schedule-detail', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.all()
        context['location'] = Location.objects.all()
        context['teacher'] = Teacher.objects.all()
        context['comment'] = Comment.objects.all()
        return context
