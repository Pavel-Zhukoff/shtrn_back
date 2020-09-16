from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView
from django.urls import reverse_lazy
from django.views import generic

from account.forms import UserLoginForm, UserRegisterForm


class LoginCustomView(UserPassesTestMixin, LoginView):
    #template_name = 'views/accounts/login.jhtml'
    authentication_form = UserLoginForm

    login_url = reverse_lazy('home') # Устанавливаем login_url на /, чтобы редиректило на главную, если пользователь авторизован

    def get_context_data(self, **kwargs):
        context = super(LoginCustomView, self).get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated


class RegisterCustomView(UserPassesTestMixin, generic.CreateView):
    form_class = UserRegisterForm
    #template_name = 'views/accounts/register.jhtml'

    success_url = reverse_lazy('login')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(RegisterCustomView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated


class PasswordResetCustomView(PasswordResetView):
    #form_class = UserRegisterForm
    #template_name = 'views/accounts/register.jhtml'


    def get_context_data(self, **kwargs):
        context = super(PasswordResetCustomView, self).get_context_data(**kwargs)
        context['title'] = 'Восстановление пароля'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated


class PasswordResetConfirmCustomView(PasswordResetConfirmView):
    #form_class = UserRegisterForm
    #template_name = 'views/accounts/register.jhtml'

    #sucess_url=

    def get_context_data(self, **kwargs):
        context = super(PasswordResetConfirmCustomView, self).get_context_data(**kwargs)
        context['title'] = 'Восстановление пароля'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated