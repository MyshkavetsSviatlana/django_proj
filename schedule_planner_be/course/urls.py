from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<slug:slug>/delete', CourseDeleteView.as_view(), name='course_confirm_delete'),
    path('courses/<slug:slug>/edit', CourseUpdateView.as_view(), name='course_edit'),
    path('courses/new/', CourseCreateView.as_view(), name='course_form'),
    path('courses/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]

