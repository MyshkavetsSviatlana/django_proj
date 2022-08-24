from django.contrib import admin
from .models import Course, Comment


class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_name", "course_type", "location", "start_date", "start_time", "start_day_of_week", "days_of_week",
                    "number_of_lessons", "end_date", "transit_date_1", "transit_date_2", "all_course_days"]
    ordering = ["-id"]


admin.site.register(Course, CourseAdmin)
admin.site.register(Comment)