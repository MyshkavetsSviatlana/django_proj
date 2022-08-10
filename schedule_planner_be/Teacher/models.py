from django.db import models
from datetime import datetime


# import Teacher_services


class Teacher(models.Model):
    """Преподаватели"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    start_date = models.DateField()
    group_count = models.PositiveSmallIntegerField("Количество групп", default=0)
    prog_language = models.CharField("Язык программирования", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="Teachers/")

    @property
    def full_experience(self):
        int_day = datetime.now() - self.start_date
        suffix = ("год" if 11 <= int_day <= 19 or int_day % 10 == 1 else
                  "года" if 2 <= int_day % 10 <= 4 else "лет")
        return f"{int_day} {suffix}"

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teacher"
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
