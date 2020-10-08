from django.db import models


class SubjectModel(models.Model):

    name = models.CharField('Название', max_length=45)
    description = models.TextField('Описание')
    price = models.IntegerField('Стоимость')
    slug = models.SlugField('Ссылка', unique=True)

    def get_absolute_url(self):
        return '/subject/{}/'.format(self.slug)

    class Meta:
        db_table = 'subjects'
        verbose_name = 'дисциплина'
        verbose_name_plural = 'дисциплины'
