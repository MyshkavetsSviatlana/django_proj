from rest_framework import serializers
from Teacher.models import Teacher


class TeacherListSerializer(serializers.ModelSerializer):
    """Список преподавателей"""
    class Meta:
        model = Teacher
        fields = ('id', 'name',)


class TeacherDetailSerializer(serializers.ModelSerializer):
    """Полное описание преподавателя"""
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherCreateSerializer(serializers.ModelSerializer):
    """Добавление преподавателя"""
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherUpdateSerializer(serializers.ModelSerializer):
    """Добавление преподавателя"""
    class Meta:
        model = Teacher
        fields = ['image', 'description']


class TeacherDeleteSerializer(serializers.ModelSerializer):
    """Добавление преподавателя"""
    class Meta:
        model = Teacher
        fields = '__all__'
