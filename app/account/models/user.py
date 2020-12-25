from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail

from django.db import models

from account.models.managers import UserManager
from account.utils import send_sms, normalize_phone


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('Электронная почта', unique=True, null=True)
    phone = models.CharField('Телефон', max_length=11, unique=True)
    password = models.CharField('Пароль', max_length=200)

    first_name = models.CharField('Имя', max_length=30, null=True)
    last_name = models.CharField('Фамилия', max_length=30, null=True)
    third_name = models.CharField('Отчество', max_length=30, null=True, blank=True, default='')

    register_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField('Аккаунт подтвержден', default=True)
    is_staff = models.BooleanField('Сотрудник', default=False)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    backend = 'account.backends.CustomAuthMiddleware'

    objects = UserManager()

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.third_name)

    get_full_name.short_description = 'ФИО'
    get_full_name.admin_order_field = 'last_name'

    def get_short_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    get_short_name.short_description = 'Имя'


    def sms_user(self, message):
        send_sms(self.phone, message)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        self.phone = normalize_phone(self.phone)
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'
