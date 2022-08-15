from rest_framework import serializers
from Teacher.models import Teacher


class TeacherListSerializer(serializers.ModelSerializer):
    """Список преподавателей"""
    class Meta:
        model = Teacher
        fields = ('id', 'surname', 'name')


class TeacherDetailSerializer(serializers.ModelSerializer):
    """Полное описание преподавателя, добавление и удаление преподавателя"""
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherUpdateSerializer(serializers.ModelSerializer):
    """Изменение преподавателя"""
    class Meta:
        model = Teacher
        fields = ['surname', 'name', 'specialization']


