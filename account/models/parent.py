from django.db import models

from account.models import User
from account.utils import send_sms


class ParentModel(models.Model):

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    third_name = models.CharField('Отчество', max_length=30)
    phone = models.CharField('Телефон', max_length=11, unique=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.third_name)

    def get_short_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def sms_user(self, message):
        send_sms(self.phone, message)

    class Meta:
        db_table = 'parents'
        verbose_name = 'родитель'
        verbose_name_plural = 'родители'