from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Создание модели пользователя"""
    email = models.EmailField(_('email address'), max_length=150, unique=True,
                              help_text=_('Enter email in format example@gmail.ru'), validators=[
        RegexValidator(
            regex="^([A-Za-z0-9]{1}[-!#$%&'*+./=?^_`{}|~A-Za-z0-9]{,63})@([a-z]{1,}\.){1,2}[a-z]{2,6}$",
            message=_('Write correct email address'),
            code=_('invalid_email')
        ),
    ])
    ROLE_CHOICES = [
        ('Super Admin', 'Super Admin'),
        ('Administrator', 'Administrator'),
        ('Manager', 'Manager'),
    ]
    role = models.CharField(_('Role'), max_length=15, choices=ROLE_CHOICES, default='Manager')
    first_name = models.CharField(_('First name'), max_length=50, blank=True)
    last_name = models.CharField(_('Last name'), max_length=100, blank=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now=True)
    image = models.ImageField(_('Photo'), upload_to='Users/', blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



