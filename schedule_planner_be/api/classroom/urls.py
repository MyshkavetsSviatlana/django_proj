from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassroomListView.as_view()),
    path('<int:pk>/', views.ClassroomDetailsView.as_view()),
    #     # path('new/', views.UserCreateView.as_view()),
]
