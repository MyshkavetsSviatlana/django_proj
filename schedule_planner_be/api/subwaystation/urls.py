from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubwayStationListView.as_view()),
    path('<int:pk>/', views.SubwayStationDetailsView.as_view()),
    #     # path('new/', views.UserCreateView.as_view()),
]
