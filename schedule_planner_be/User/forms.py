from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import User
from .service import send


class UserAuthenticationForm(AuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if not self.user_cache.email_verify:
                send(self.request, self.user_cache)
                raise ValidationError(
                    'Email not verify, check you email',
                    code='invalid login'
                )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserCreationForm(forms.ModelForm):
    """Форма для создания нового пользователя"""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, validators=[
        RegexValidator(
            regex="^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$",
            message=_('Write correct password'),
            code=_('invalid_password')
        )], help_text=_('Password should have at least one digit, one upper case letter and one lower case letter'))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'image')

    def clean_passwords(self):
        """Проверка на совпадение паролей"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Сохранение предоставленного пароль в хешированном формате"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
