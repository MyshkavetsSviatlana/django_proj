from datetime import datetime, timedelta, date

from django.db import models
from django.db.backends.signals import connection_created
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.urls import reverse
from course.models import Course, Comment, ClassroomAvailability, Lesson


class SubwayStation(models.Model):
    """Creates model Subway station"""
    station = models.CharField('Subway station', max_length=50, default=None)

    def __str__(self):
        return f"с/м {self.station}"

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'


class Location(models.Model):
    """"Creates model Location"""
    city = models.CharField('City', max_length=50)
    street = models.CharField('Street', max_length=50)
    building = models.CharField('Building', max_length=10, default=None)
    subway = models.ForeignKey(SubwayStation, on_delete=models.SET_NULL, null=True, verbose_name='Станции метро')

    def __str__(self):
        return f"{self.street}, {self.building}, {self.subway}, {self.city}"

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Classroom(models.Model):
    """Creates model Classroom"""
    classroom = models.CharField('Classroom', max_length=10)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    seats_number = models.PositiveSmallIntegerField("Number of seats")
    pc_number = models.PositiveSmallIntegerField("Number of PCs")

    def __str__(self):
        return f"ауд. {self.classroom}, {self.location}"

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        unique_together = ('classroom', 'location')


# class Availability(AbstractAvailability):
#     class AgendaMeta:
#         schedule_model = Classroom
#         schedule_field = "classroom"  # optional


# class AvailabilityOccurrence(AbstractAvailabilityOccurrence):
#     class AgendaMeta:
#         availability_model = Availability
#         schedule_model = Classroom
#         schedule_field = "classroom"  # optional
#
#
# class TimeSlot(AbstractTimeSlot):
#     class AgendaMeta:
#         availability_model = Availability
#         schedule_model = Classroom
#         booking_model = "ClassroomReservation"  # booking class, more details shortly
#         schedule_field = "classroom"  # optional


# class ClassroomReservation(AbstractBooking):
#     class AgendaMeta:
#         schedule_model = Classroom
#
#     owner = models.ForeignKey(
#         to=settings.AUTH_USER_MODEL,
#         on_delete=models.PROTECT,
#         related_name="reservations",
#     )
#     start_time = models.DateTimeField(db_index=True)
#     end_time = models.DateTimeField(db_index=True)
#     approved = models.BooleanField(default=False)
#
#     def get_reserved_spans(self):
#         # we only reserve the time if the reservation has been approved
#         if self.approved:
#             yield TimeSpan(self.start_time, self.end_time)


class Schedule(models.Model):
    """Создание модели Расписание"""

    title = models.TextField(default=None)
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='Курсы')
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name='Локации')
    reviews = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, verbose_name='Комментарии')
    url = models.SlugField(max_length=160, unique=True, default=None)

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.courses}"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


@receiver(post_save, sender=Classroom)
def classroom_availability(sender, instance, **kwargs):
    """"Creates classroom availabilities for 30 days period after classroom creation"""
    start_range_date = date.today()
    number_of_days = 30
    date_list = []
    for day in range(number_of_days):
        a_date = (start_range_date + timedelta(days=day)).isoformat()
        date_list.append(a_date)
    classroom = instance
    start_time_range = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
                        "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
    for item in date_list:
        for start_time_option in start_time_range:
            # available from 8 AM to 22 PM
            ClassroomAvailability.objects.create(
                classroom=classroom,
                date=item,
                start_time=start_time_option,
            )


@receiver(post_save, sender=Lesson)
def reserve_classroom(sender, instance, **kwargs):
    """"Reserves classroom availability"""
    lesson = instance
    date = lesson.date
    classroom = lesson.location
    start_time = lesson.start_time
    slot = ClassroomAvailability.objects.filter(date=date, classroom=classroom, start_time=start_time)
    slot.update(is_free=False)


@receiver(post_save, sender=Lesson)
def delete_old_classroomavailabilities(sender, instance, **kwargs):
    """"Deletes classroom availabilities for past dates"""
    today = date.today()
    ClassroomAvailability.objects.filter(date__lt=today).delete()


@receiver(post_delete, sender=Lesson)
def make_classroomavailability_free(sender, instance, **kwargs):
    """"Returns free status to classroom availabilities"""
    lesson = instance
    date = lesson.date
    classroom = lesson.location
    start_time = lesson.start_time
    slot = ClassroomAvailability.objects.filter(date=date, classroom=classroom, start_time=start_time)
    slot.update(is_free=True)


@receiver(post_delete, sender=Classroom)
def delete_cl_av_for_deleted_classrooms(sender, instance, **kwargs):
    """"Deletes classroom availabilities for deleted classrooms"""
    classroom = instance
    location = classroom.location
    classroom = classroom.classroom
    address = f'ауд. {classroom}, {location}'
    ClassroomAvailability.objects.filter(classroom=address).delete()


@receiver(connection_created)
def create_cl_av_for_90_days_period(sender, *args, **kwargs):
    """"Updates classroom availabilities for 90 days period"""
    classrooms = Classroom.objects.all()
    for classroom in classrooms:
        cla_av = ClassroomAvailability.objects.filter(classroom=classroom).values('date')
        last_cl_av_date_dict = cla_av.latest('date', 'start_time')
        last_cl_av_date = last_cl_av_date_dict.get('date')
        date_today = date.today()
        td = timedelta(days=90)
        date_in_90_days = date_today + td
        number_of_days = date_in_90_days - last_cl_av_date
        number_of_days = number_of_days.days
        date_list = []
        for day in range(number_of_days):
            a_date = (last_cl_av_date + timedelta(days=day)).isoformat()
            date_list.append(a_date)
        start_time_range = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
                            "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
        del date_list[0]
        for item in date_list:
            for start_time_option in start_time_range:
                # available from 8 AM to 22 PM
                ClassroomAvailability.objects.create(
                    classroom=classroom,
                    date=item,
                    start_time=start_time_option,
                )
