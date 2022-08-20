from rest_framework import serializers
from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Список курсов"""
    class Meta:

        model = Course
        fields = '__all__'

    def create(self, validated_data):
        return Course.objects.create(**validated_data)