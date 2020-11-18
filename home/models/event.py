from django.db import models

import account.models


class EventModel(models.Model):

    name = models.CharField('Название', max_length=100)
    content = models.TextField('Описание')
    start_date = models.DateTimeField('Дата и время начала')
    finish_date = models.DateTimeField('Дата и время окончания')
    slug = models.SlugField('Ссылка', unique=True)

    students = models.ManyToManyField(account.models.StudentModel, verbose_name='Участники')

    def get_absolute_url(self):
        return '/events/{}/'.format(self.slug)

    class Meta:
        db_table = 'events'
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'
