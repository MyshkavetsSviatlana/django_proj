from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    """Создание модели пользователя"""
    ROLE_CHOICES = [
        ('SuperAdmin', 'SuperAdmin'),
        ('Administrator', 'Administrator'),
        ('Manager', 'Manager'),
        ('Teacher', 'Teacher')
    ]
    fist_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField(max_length=150, unique=True, validators=[
        RegexValidator(
            regex="^([A-Za-z0-9]{1}[-!#$%&'*+./=?^_`{}|~A-Za-z0-9]{,63})@([a-z]{1,}\.){1,2}[a-z]{2,6}$",
            message='Write correct email address',
            code='invalid_email'
        ),
    ])
    role = models.CharField('Роль',max_length=15, choices=ROLE_CHOICES, null=True)

    def __str__(self):
        return f'{self.fist_name} {self.last_name} : {self.role}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



