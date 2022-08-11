from django.urls import path
from . import views

urlpatterns =[
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailsView.as_view()),
    # path('new/', views.UserCreateView.as_view()),
]