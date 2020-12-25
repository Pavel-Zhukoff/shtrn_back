from django.db import models

from account.models import User
from account.models.parent import ParentModel
from .grade import GradeModel


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

    school = models.CharField('Школа', max_length=100)

    year_of_study = models.ForeignKey(GradeModel, on_delete=models.RESTRICT, verbose_name='Класс')
    parent = models.ForeignKey(ParentModel, on_delete=models.RESTRICT, verbose_name='Родитель')

    user = models.OneToOneField(User, on_delete=models.RESTRICT, verbose_name='Пользователь')

    @property
    def first_name(self):
        return self.user.first_name

    @first_name.setter
    def first_name(self, value):
        self.user.first_name = str(value).strip().capitalize()

    @property
    def last_name(self):
        return self.user.last_name

    @last_name.setter
    def last_name(self, value):
        self.user.last_name = str(value).strip().capitalize()

    @property
    def third_name(self):
        return self.user.third_name

    @third_name.setter
    def third_name(self, value):
        self.user.third_name = str(value).strip().capitalize()

    @property
    def phone(self):
        return self.user.phone

    @property
    def email(self):
        return self.user.email

    def get_full_name(self):
        return self.user.get_full_name()

    def get_short_name(self):
        return self.user.get_short_name()

    def get_school_info(self):
        return '{}, {} класс'.format(self.school, self.phone)
    get_school_info.short_description = 'Класс'

    class Meta:
        db_table = 'students'
        verbose_name = 'ученика'
        verbose_name_plural = 'ученики'
