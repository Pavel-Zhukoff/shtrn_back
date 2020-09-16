from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(label='Электронная почта', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': ''
        }
    ))
    password1 = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': '',
        }
    ))
    password2 = forms.CharField(label='Повтор пароля', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': '',
        }
    ))

