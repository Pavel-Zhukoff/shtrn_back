from django.db import models

from account.models import User
from account.utils import send_sms


class StudentModel(models.Model):

    SCHOOL_CLASSES = [
        (1, 'первый'),
        (2, 'второй'),
        (3, 'третий'),
        (4, 'четвертый'),
        (5, 'пятый'),
        (6, 'шестой'),
        (7, 'седьмой'),
        (8, 'восьмой'),
        (9, 'девятый'),
        (10, 'десятый'),
        (11, 'одиннадцатый'),
    ]

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    third_name = models.CharField('Отчество', max_length=30)
    phone = models.CharField('Телефон', max_length=11)
    school = models.CharField('Учебное заведение', max_length=100)
    year_of_study = models.CharField('Год обучения', max_length=2, choices=SCHOOL_CLASSES)

    parent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Родитель')

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.third_name)
    get_full_name.short_description = 'ФИО'


    def get_short_name(self):
        return '{} {}'.format(self.last_name, self.first_name)
    get_short_name.short_description = 'Имя'


    def get_school_info(self):
        return '{}, {} класс'.format(self.school, self.phone)
    get_school_info.short_description = 'Класс'


    def sms_user(self, message):
        send_sms(self.phone, message)

    class Meta:
        db_table = 'students'
        verbose_name = 'ученика'
        verbose_name_plural = 'ученики'
