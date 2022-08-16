from django.urls import path
from . import views

urlpatterns = [
    path('schedules/', views.ScheduleListView.as_view(), name='schedules'),
    path('schedule/<int:pk>/detail', views.ScheduleDetailView.as_view(), name='schedule-detail'),
    path('add-schedule/', views.ScheduleCreateView.as_view(), name='add-schedule'),
    path('delete-schedule/<int:pk>/delete', views.ScheduleDeleteView.as_view(), name='delete-schedule'),
    path('edit-schedule/<int:pk>/update', views.ScheduleUpdateView.as_view(), name='edit-schedule'),
]

urlpatterns += [
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>/detail', views.LocationDetailView.as_view(), name='location-detail'),
    path('add-location/', views.LocationCreateView.as_view(), name='add-location'),
    path('delete-location/<int:pk>/delete', views.LocationDeleteView.as_view(), name='delete-location'),
    path('edit-location/<int:pk>/update', views.LocationUpdateView.as_view(), name='edit-location'),
]

urlpatterns += [
    path('subways/', views.SubwayStationListView.as_view(), name='subways'),
    path('subway/<int:pk>/detail', views.SubwayStationDetailView.as_view(), name='subway-detail'),
    path('add-subway/', views.SubwayStationCreateView.as_view(), name='add-subway'),
    path('delete-subway/<int:pk>/delete', views.SubwayStationDeleteView.as_view(), name='delete-subway'),
    path('edit-subway/<int:pk>/update', views.SubwayStationUpdateView.as_view(), name='edit-subway'),
]
