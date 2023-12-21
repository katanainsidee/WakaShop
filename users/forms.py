from django.forms import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:

        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'placeholder': 'Имя пользователя'
            }),
            "password": PasswordInput(attrs={
                'placeholder': 'Пароль'
            })
        }