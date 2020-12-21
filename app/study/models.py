from django.db import models
from django.urls import reverse_lazy

from random import randint as rnd

import home.models
import account.models
from study.utils import slugify


class RoomModel(models.Model):

    name = models.CharField('Название комнаты', max_length=100, null=False)

    slug = models.SlugField('Ярлык комнаты', null=True, blank=True, unique=True)

    start_date = models.DateTimeField('Время старта')
    finish_date = models.DateTimeField('Время окончания')

    speakers = models.ManyToManyField(home.models.TeacherModel, verbose_name='Докладчики', related_name='speaker')
    users = models.ManyToManyField(account.models.User, verbose_name='Участники', related_name='visitor')

    def clean(self):
        super().clean()
        self.name = self.name.strip()
        if self.slug is None:
            self.slug = slugify('{}-{}'.format(self.name.lower(), rnd(0, 9999)))
        else:
            self.slug = self.slug.lower()

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify('{}-{}'.format(self.name.lower(), rnd(0, 9999)))
        else:
            self.slug = self.slug.lower()
        super(RoomModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('study:room', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'комнаты'
        verbose_name_plural = 'комнаты'
        db_table = 'room'