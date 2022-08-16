from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view()),
    path('<int:pk>/', views.CourseDetailsView.as_view()),
    #     # path('new/', views.UserCreateView.as_view()),
]
