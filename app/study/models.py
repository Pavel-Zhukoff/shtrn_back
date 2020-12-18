from django.db import models
from django.urls import reverse_lazy

import home.models
import account.models


class RoomModel(models.Model):

    name = models.CharField('Название комнаты', max_length=100, null=False)

    slug = models.SlugField('Ярлык комнаты', unique=True)

    start_date = models.DateTimeField('Время старта')
    finish_date = models.DateTimeField('Время окончания')

    speakers = models.ManyToManyField(home.models.TeacherModel, verbose_name='Докладчики', related_name='speaker')
    users = models.ManyToManyField(account.models.User, verbose_name='Участники', related_name='visitor')

    def get_absolute_url(self):
        return reverse_lazy('study:room', args=[self.slug])

    class Meta:
        verbose_name = 'комнаты'
        verbose_name_plural = 'комнаты'
        db_table = 'room'