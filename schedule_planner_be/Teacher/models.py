from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    """Преподаватели"""
    surname = models.CharField(_("Surname"), max_length=50, validators=[
        RegexValidator(
            regex="^[А-яа-я]{1,50}$",
            message=_('Write correct surname'),
            code=_('invalid_surname')
        ),
    ])
    name = models.CharField(_("Name"), max_length=50, validators=[
        RegexValidator(
            regex="^[А-яа-я]{1,50}$",
            message=_('Write correct name'),
            code=_('invalid_name')
        ),
    ])
    fathers_name = models.CharField(_("Father's name"), max_length=50, blank=True, validators=[
        RegexValidator(
            regex="^[А-яа-я]{1,50}$",
            message=_("Write correct father's name"),
            code=_('invalid_fathers_name')
        ),
    ])
    age = models.PositiveSmallIntegerField(_("Age"), default=0, blank=True)
    start_date = models.DateField(_('Start date of teaching'), blank=True, default=timezone.now)
    group_count = models.PositiveSmallIntegerField(_("Number of groups"), default=0, blank=True)
    specialization = models.CharField(_("Specialization"), max_length=250, validators=[
        RegexValidator(
            regex="^[А-яа-я]{1,250}$",
            message=_("Write correct specialization"),
            code=_('invalid_specialization')
        ),
    ])
    phone = models.CharField(_('Phone'), max_length=25, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(_("Photo"), upload_to="Teachers/", blank=True)
    url = models.SlugField(max_length=160, unique=True, default=None)

    def __str__(self):
        return f"{self.surname} {self.name}"

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'slug': self.url})

    class Meta:
        db_table = "teacher"
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
