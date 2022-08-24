from django.urls import path
from . import views

urlpatterns =[
    path('', views.TeacherListView.as_view(), name='get_all_teachers'),
    path('edit/<int:pk>/', views.TeacherUpdateView.as_view(), name='edit_teacher'),
    path('delete/<int:pk>/', views.TeacherDeleteView.as_view()),
    path('<int:pk>/', views.TeacherDetailsView.as_view()),
    path('new/', views.TeacherCreateView.as_view()),
]