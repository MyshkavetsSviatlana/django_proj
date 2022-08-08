from django.urls import path
from .views import ScheduleUpdateView, ScheduleDeleteView, ScheduleDetailView, ScheduleCreateView, ScheduleListView

urlpatterns = [
    path('schedules/', ScheduleListView.as_view(), name='schedules'),
    path('schedule/<int:pk>/detail', ScheduleDetailView.as_view(), name='schedule-detail'),
    path('add-schedule/', ScheduleCreateView.as_view(), name='add-schedule'),
    path('delete-schedule/<int:pk>/delete', ScheduleDeleteView.as_view(), name='delete-schedule'),
    path('edit-schedule/<int:pk>/update', ScheduleUpdateView.as_view(), name='edit-schedule'),
]
