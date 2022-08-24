from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserListSerializer, UserCreateSerializer
from User.models import User


class UserListView(generics.ListAPIView):
    """Вывод списка пользователей"""
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateView(generics.CreateAPIView):
    """Добавление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

