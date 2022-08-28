from django_filters import rest_framework as filters, DateFromToRangeFilter
from course.models import Lesson


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class LessonFilter(filters.FilterSet):
    """Фильтрация по имени курса, учителю, локации"""
    date = DateFromToRangeFilter(field_name='date')

    class Meta:
        model = Lesson
        fields = ['course__course_name', 'teacher', 'course__location', 'date']