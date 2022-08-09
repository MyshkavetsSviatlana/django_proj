from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы зарегестрировались на нашем сайте',
        'С уважением, Академия BelHard!',
        'ag.charniauskaya@gmail.com',
        [user_email],
        fail_silently=False
    )