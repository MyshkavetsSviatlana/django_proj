from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'),
         name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', views.EmailVerify.as_view(),
         name="verify_email",
    ),
    path(
        'invalid_verify/', TemplateView.as_view(
            template_name='registration/invalid_verify.html'
        ),
        name='invalid_verify'

    ),
    # path('send_repeat_message/', views.SendRepeadMessage.as_view(),
    #      name='send_repeat_message')
]