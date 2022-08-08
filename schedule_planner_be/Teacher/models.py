from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class Teacher(models.Model):
    """Преподаватели"""
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    start_date = models.DateField()
    group_count = models.PositiveSmallIntegerField("Количество групп", default=0)
    prog_language = models.CharField("Язык программирования", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="Teachers/")
    url = models.SlugField(max_length=160, unique=True, default=None)

    def __str__(self):
        return self.name

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


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание модели пользователя при регистрации"""
    if created:
        TeacherProfile.objects.create(user=instance)


@receiver(post_save, sender=Teacher)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
