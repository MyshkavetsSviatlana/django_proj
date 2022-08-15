from rest_framework import serializers
from course.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    """Список курсов"""
    class Meta:

        model = Course
        fields = '__all__'

