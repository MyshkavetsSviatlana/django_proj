from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<slug:slug>/delete', CourseDeleteView.as_view(), name='course_confirm_delete'),
    path('<slug:slug>/edit', CourseUpdateView.as_view(), name='course_edit'),
    path('new/', CourseCreateView.as_view(), name='course_form'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('comment/', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('<int:pk>/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/new/', CommentCreateView.as_view(), name='comment_form'),
    path('comment/<slug:slug>/delete', CommentDeleteView.as_view(), name='comment_confirm_delete'),
    path('lesson/morning', LessonMorningListView.as_view(), name='lesson_morning_list'),
    path('lesson/morning/filter', FilterMorningLessonView.as_view(), name='morning_filter'),
    path('lesson/evening', LessonEveningListView.as_view(), name='lesson_evening_list'),
    path('lesson/evening/filter', FilterEveningLessonView.as_view(), name='evening_filter'),
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/filter', FilterLessonView.as_view(), name='filter'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/edit/', LessonUpdateView.as_view(), name='lesson_edit'),
    path('lesson/new/', LessonCreateView.as_view(), name='lesson_form'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_confirm_delete'),
]

