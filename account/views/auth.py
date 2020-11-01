import random

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from account.business import create_user_verification
from account.forms import UserRegisterForm, UserLoginForm, PasswordChangeForm
from account.forms import UserCodeConfirmForm
from account.models import User, VerificationModel
from account.utils import build_url, send_sms, normalize_phone


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            phone, code = create_user_verification(form.cleaned_data)
            # send_sms(phone, 'Код подтверждения - {}'.format(code))
            return HttpResponseRedirect(build_url('account:code_verification', params={'phone': phone}))
    else:
        form = UserRegisterForm()
    return render(request,
                  'account/form.jhtml',
                  {'form': form, 'title': 'Регистрация'})


def code_verification(request):
    phone = request.GET.get('phone', None)
    if phone is None:
        return HttpResponseRedirect(reverse_lazy('account:register'))
    phone = normalize_phone(phone)
    form = UserCodeConfirmForm(initial={'phone': phone})
    if request.method == 'POST':
        form = UserCodeConfirmForm(request.POST)
        if form.is_valid():
            user = verify_user(form.cleaned_data.get('code'), phone)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('account:main-page'))
            form.errors['code'] = ['Неверный код верификации']

    return render(request,
                  'account/form.jhtml',
                  {'form': form, 'title': 'Подтверждение пароля'})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = normalize_phone(form.cleaned_data.get('username'))
            user = auth.authenticate(request, username=username, password=form.cleaned_data.get('password'))
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('account:main-page'))
            form.errors['username'] = ['Неправильный логин или пароль']
    else:
        form = UserLoginForm()
    return render(request,
                  'account/form.jhtml',
                  {'form': form, 'title': 'Регистрация'})


@login_required(login_url='/account/login')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('home:main-page'))


@login_required(login_url='/account/login')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password') == form.cleaned_data.get('match_password'):
                change_password(request.user, form.cleaned_data.get('password'))
                return HttpResponseRedirect(reverse_lazy('account:main-page'))
            else:
                form.errors['password'] = ['Пароли не совпадают']
    else:
        form = PasswordChangeForm()

    return render(request,
                  'account/form.jhtml',
                  {'form': form, 'title': 'Смена пароля'})
