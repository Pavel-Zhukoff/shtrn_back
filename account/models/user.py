from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail

from django.db import models

from account.models.managers import UserManager
from account.utils import send_sms


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('Электронная почта', unique=True, null=True)
    phone = models.CharField('Номер телефона', max_length=11, unique=True)
    password = models.CharField('Пароль', max_length=200)
    register_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField('Верификация', default=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def sms_user(self, message):
        send_sms(self.phone, message)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'