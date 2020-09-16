from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(label='Электронная почта', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': ''
        }
    ))
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': '',
        }
    ))


