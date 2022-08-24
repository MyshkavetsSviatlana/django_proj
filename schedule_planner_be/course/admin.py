from django.contrib import admin
from .models import Course, Comment

#
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ["course_name", "all_course_dates"]
#     ordering = ["-id"]
#     search_fields = ["course_name"]
#     list_filter = ["course_type", "teacher"]
#

admin.site.register(Course)
admin.site.register(Comment)


