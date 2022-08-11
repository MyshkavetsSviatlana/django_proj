from rest_framework import generics
from .serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer
from User.models import User


class UserListView(generics.ListAPIView):
    """Вывод списка пользователей"""
    serializer_class = UserListSerializer

    def get_queryset(self):
        users = User.object.all()
        return users


class UserDetailsView(generics.RetrieveAPIView):
    """Вывод полного описания пользователя"""
    queryset = User.object.filter()
    serializer_class = UserDetailSerializer


# class UserCreateView(generics.CreateAPIView):
#     """Добавление пользователя"""
#     serializer_class = UserCreateSerializer



