from django.urls import path
from .views import TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher_list'),
    path('<slug:slug>/delete', TeacherDeleteView.as_view(), name='teacher_confirm_delete'),
    path('<slug:slug>/edit', TeacherUpdateView.as_view(), name='teacher_edit'),
    path('new/', TeacherCreateView.as_view(), name='teacher_form'),
    path('<slug:slug>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_profile/<int:pk>/', ShowProfilePageView.as_view(), name='teacher_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_teacher_profile'),
]