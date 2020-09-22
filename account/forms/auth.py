from django import forms


class UserRegisterForm(forms.Form):
    phone = forms.CharField(label='Телефон', required=True, widget=forms.TextInput())


class UserCodeConfirmForm(forms.Form):
    phone = forms.CharField(label='Телефон', required=False, widget=forms.TextInput(attrs={'disabled': True}))
    code = forms.CharField(label='Код подтверждения', max_length=8, widget=forms.TextInput())


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Телефон', required=True, widget=forms.TextInput())
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput())

