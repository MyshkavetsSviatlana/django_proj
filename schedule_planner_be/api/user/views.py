from rest_framework import generics
from .serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer
from User.models import User


class UserListView(generics.ListAPIView):
    """Вывод списка пользователей"""
    serializer_class = UserListSerializer

    def get_queryset(self):
        users = User.objects.all()
        return users


class UserDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания пользователя"""
    queryset = User.objects.filter()
    serializer_class = UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    """Добавление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
