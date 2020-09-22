import random

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy


from account.forms import UserRegisterForm, UserLoginForm
from account.forms import UserCodeConfirmForm
from account.models import User, VerificationModel
from account.utils import build_url, send_sms, normalize_phone


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            phone = normalize_phone(form.cleaned_data.get('phone'))
            code = random.randint(10000000, 99999999) % 10000000
            print(code)
            #send_sms(phone, 'Код подтверждения - {}'.format(code))
            verify = VerificationModel()
            verify.phone = phone
            verify.code = code
            verify.save()
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
    form = UserCodeConfirmForm()
    form.fields['phone'].widget.attrs['value'] = phone
    if request.method == 'POST':
        form = UserCodeConfirmForm(request.POST)
        verification = VerificationModel.objects.get(phone=phone)
        if form.is_valid():
            confirm = form.cleaned_data
            if confirm.get('code') == verification.code:
                user = User.objects.create_user(phone, verification.code)
                user.save()
                auth.login(request, user)
                verification.delete()
                return HttpResponseRedirect(reverse_lazy('account:main-page'))

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


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('home:main-page'))