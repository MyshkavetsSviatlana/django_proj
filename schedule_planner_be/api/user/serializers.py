from django.core.validators import RegexValidator
from rest_framework import serializers
from User.models import User
# from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserListSerializer(serializers.ModelSerializer):
    """Список пользователей"""
    class Meta:
        model = User
        fields = ('id', 'email',)


class UserCreateSerializer(serializers.ModelSerializer):
    """Добавление пользователя"""
    password = serializers.CharField(label='Password', validators=[
        RegexValidator(
            regex="^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8}$",
            message=_('Write correct password'),
            code=_('invalid_password')
        )], help_text=_('Password should have at least one digit, one upper case letter and one lower case letter'),
                                      write_only=True)
    # password_2 = serializers.CharField(label='Password confirmation', write_only=True)
    #
    # def clean_passwords(self, validated_data):
    #     """Проверка на совпадение паролей"""
    #     password = validated_data.pop("password")
    #     password_2 = validated_data.pop("password2")
    #     if password and password_2 and password != password_2:
    #         raise ValidationError("Passwords don't match")
    #     return password

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'image', 'password')

    def create(self, validated_data):
        """Сохранение предоставленного пароль в хешированном формате"""
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(self.validated_data["password"])
        user.save()
        return user