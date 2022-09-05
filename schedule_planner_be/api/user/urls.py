from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.LoginAPIView.as_view(), name='login-api'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('email_verify/', views.VerifyEmail.as_view(), name='email-verify'),
]
