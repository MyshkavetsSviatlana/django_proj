from django.urls import path
from . import views
# from . import api


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]