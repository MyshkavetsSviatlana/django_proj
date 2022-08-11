from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<slug:slug>/delete', CourseDeleteView.as_view(), name='course_confirm_delete'),
    path('<slug:slug>/edit', CourseUpdateView.as_view(), name='course_edit'),
    path('new/', CourseCreateView.as_view(), name='course_form'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]

