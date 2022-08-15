from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, \
    CommentListView, CommentCreateView, CommentDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<slug:slug>/delete', CourseDeleteView.as_view(), name='course_confirm_delete'),
    path('<slug:slug>/edit', CourseUpdateView.as_view(), name='course_edit'),
    path('new/', CourseCreateView.as_view(), name='course_form'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('comment/', CommentListView.as_view(), name='comment_list'),
    path('comment/new/', CommentCreateView.as_view(), name='comment_form'),
    path('comment/<slug:slug>/delete', CommentDeleteView.as_view(), name='comment_confirm_delete'),
]

