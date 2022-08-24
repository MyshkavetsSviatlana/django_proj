from django_filters import rest_framework as filters
from course.models import Course


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CourseFilter(filters.FilterSet):
    """Фильтрация по имени курса, учителю, локации"""
    # start_date = DateFilter(field_name='from date', lookup_expr=('gt'))
    # end_date = DateFilter(field_name='to date', lookup_expr=('lt'))

    class Meta:
        model = Course
        fields = ['course_name', 'teacher', 'location', 'all_course_days']