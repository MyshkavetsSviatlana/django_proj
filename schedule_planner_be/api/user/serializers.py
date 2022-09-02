from django.core.validators import RegexValidator
from rest_framework import serializers
from User.models import User
# from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    """Добавление пользователя"""
    password = serializers.CharField(label='Password', validators=[
        RegexValidator(
            regex="^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8}$",
            message=_('Invalid password'),
            code=_('invalid_password')
        )], help_text=_('Password should have only 8 characters, '
                        'at least one digit, one upper case letter and one lower case letter'),
                                      write_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'role', 'password')

    def create(self, validated_data):
        """Создание пользователя, сохранение предоставленного пароля в хешированном формате"""
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(self.validated_data["password"])
        user.save()
        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    tokens = serializers.CharField(max_length=555, read_only=True)
    email = serializers.CharField(max_length=555)
    password = serializers.CharField(max_length=555)

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ('email', 'password', 'tokens')

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)
        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using' + filtered_user_by_email[0].auth_provider
            )
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.email_verify:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'tokens': user.tokens
        }

