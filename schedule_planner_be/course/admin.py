from django.contrib import admin
from .models import Course, Comment, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_name", "course_type", "teacher", "location", "start_date", "start_time",
                    "start_day_of_week", "days_of_week", "number_of_lessons", ]
    ordering = ["-id"]
    search_fields = ["course_name"]
    list_filter = ["course_type", "teacher"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["number", "course", "date", "start_time", "topic", "description"]
    ordering = ["number"]
    search_fields = ["topic"]
    list_filter = ["course__course_name", "teacher", "date", "start_time"]


# admin.site.register(Course, CourseAdmin)
admin.site.register(Comment)
