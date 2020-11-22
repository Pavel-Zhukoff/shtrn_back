from django.db import models

from account.models import User
from .grade import GradeModel
from account.utils import send_sms, normalize_phone


class StudentModel(models.Model):

    SCHOOL_CLASSES = [
        (1, 'Первый'),
        (2, 'Второй'),
        (3, 'Третий'),
        (4, 'Четвертый'),
        (5, 'Пятый'),
        (6, 'Шестой'),
        (7, 'Седьмой'),
        (8, 'Восьмой'),
        (9, 'Девятый'),
        (10, 'Десятый'),
        (11, 'Одиннадцатый'),
    ]

    last_name = models.CharField('Фамилия', max_length=30)
    first_name = models.CharField('Имя', max_length=30)
    third_name = models.CharField('Отчество', max_length=30, blank=True)
    phone = models.CharField('Телефон', max_length=11, unique=True)
    school = models.CharField('Школа', max_length=100)

    year_of_study = models.ForeignKey(GradeModel, on_delete=models.CASCADE, verbose_name='Класс')
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

    def __str__(self):
        return self.get_short_name()

    def save(self, *args, **kwargs):
        self.phone = normalize_phone(self.phone)
        super(StudentModel, self).save(*args, **kwargs)

    class Meta:
        db_table = 'students'
        verbose_name = 'ученика'
        verbose_name_plural = 'ученики'
