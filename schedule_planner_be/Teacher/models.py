from django.db import models


class Teacher(models.Model):
    """Преподаватели"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    """По задумке указывается дата с момента начала преподавательского/рабочего стажа
    и автоматически поле обновляется с течением времени, плюсом от временного промежутка
    присваивается "степень" : до 1 года - Junior, 1-3 года - Middle, 3 года и более - Senior"""
    experience = models.DateField("Опыт работы")
    group_count = models.PositiveSmallIntegerField("Количество групп", default=0)
    prog_language = models.CharField("Язык программирования", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="Teachers/")

    def __str__(self):
        return self.name


class Meta:
    db_table = "teacher"
    verbose_name = "Преподаватель"
    verbose_name_plural = "Преподаватели"
