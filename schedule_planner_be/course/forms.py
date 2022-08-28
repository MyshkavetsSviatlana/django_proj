from django.forms import ModelForm
from .models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
from .models import Lesson


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
