from django.db import models

from home.models import TeacherModel


class SubjectModel(models.Model):

    name = models.CharField('Название', max_length=45)
    description = models.TextField('Описание')
    price = models.IntegerField('Стоимость')
    slug = models.SlugField('Ссылка', unique=True)

    teacher = models.ForeignKey(TeacherModel, models.DO_NOTHING, verbose_name='Преподаватель')

    def get_absolute_url(self):
        return '/subject/{}/'.format(self.slug)

    class Meta:
        db_table = 'subjects'
        verbose_name = 'дисциплина'
        verbose_name_plural = 'дисциплины'
