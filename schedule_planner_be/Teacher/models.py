from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    """Преподаватели"""
    name = models.CharField(_("Name"), max_length=100)
    surname = models.CharField(_("Surname"), max_length=100)
    age = models.PositiveSmallIntegerField(_("Age"), default=0)
    start_date = models.DateField(_('Start date of teaching'))
    group_count = models.PositiveSmallIntegerField(_("Number of groups"), default=0)
    course_name = models.CharField(_("Course name"), max_length=150)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Photo"), upload_to="Teachers/")
    url = models.SlugField(max_length=160, unique=True, default=None)

    def __str__(self):
        return f"{self.surname} {self.name}"

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'slug': self.url})

    class Meta:
        db_table = "teacher"
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class TeacherProfile(models.Model):
    objects = None
    phone = models.CharField('Телефон', max_length=25)
    teacher = models.OneToOneField(Teacher, null=True, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.teacher.name)

    class Meta:
        db_table = "teacher_profile"
        verbose_name = "Профиль учителя"
        verbose_name_plural = "Профили учителей"


# @receiver(post_save, sender=Teacher)
# def create_user_profile(sender, instance, created, **kwargs):
#     """Создание модели пользователя при регистрации"""
#     if created:
#         TeacherProfile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=Teacher)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

