from django import forms

from account.utils import normalize_phone


class UserRegisterForm(forms.Form):
    phone = forms.CharField(label='Телефон', required=True, widget=forms.TextInput())

    def clean_phone(self):
        return normalize_phone(self.cleaned_data['phone'])


class UserCodeConfirmForm(forms.Form):
    phone = forms.CharField(label='Телефон', required=False, widget=forms.TextInput(attrs={'disabled': True}))
    code = forms.CharField(label='Код подтверждения', max_length=8, widget=forms.TextInput())

    def clean_phone(self):
        return normalize_phone(self.cleaned_data['phone'])

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Телефон', required=True, widget=forms.TextInput())
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput())


class PasswordChangeForm(forms.Form):
    password = forms.CharField(label='Новый пароль', required=True, widget=forms.PasswordInput())
    match_password = forms.CharField(label='Повтор пароля', required=True, widget=forms.PasswordInput())
