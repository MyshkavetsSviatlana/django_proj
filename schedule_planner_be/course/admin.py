from django.contrib import admin
from .models import Course, Comment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_name", "course_type", "teacher", "location", "start_date", "start_time",
                    "start_day_of_week", "days_of_week", "number_of_lessons", ]
    ordering = ["-id"]
    search_fields = ["course_name"]
    list_filter = ["course_type", "teacher"]


# admin.site.register(Course, CourseAdmin)
admin.site.register(Comment)