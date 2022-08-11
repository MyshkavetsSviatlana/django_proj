from rest_framework import serializers
from User.models import User


class UserListSerializer(serializers.ModelSerializer):
    """Список пользователей"""
    class Meta:
        model = User
        fields = ('id', 'email',)


class UserDetailSerializer(serializers.ModelSerializer):
    """Полное описание пользователя"""
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    """Добавление пользователя"""
    class Meta:
        model = User
        fields = '__all__'
