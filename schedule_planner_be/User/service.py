from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage

# def send(user_email):
#     send_mail(
#         'Вы зарегестрировались на нашем сайте',
#         'С уважением, Академия BelHard!',
#         'ag.charniauskaya@gmail.com',
#         [user_email],
#         fail_silently=False
#     )
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator


def send(request, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string(
        'registration/verify_email.html',
        context=context,

    )
    email = EmailMessage(
        'Verify email',
        message,
        to=[user.email]
    )
    email.send()