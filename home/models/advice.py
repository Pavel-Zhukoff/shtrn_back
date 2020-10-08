
from django.db import models


class AdviceModel(models.Model):

    name = models.CharField('Название', max_length=100)
    content = models.TextField('Текст')
    publish_date = models.DateTimeField('Дата и время публикации')
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField('Ссылка', unique=True)
    thumbnail = models.ImageField('Изображение совета', upload_to='news/%Y/%m/%d/')

    def get_absolute_url(self):
        return '/advice/{}/'.format(self.slug)

    class Meta:
        db_table = 'advices'
        verbose_name = 'совет'
        verbose_name_plural = 'советы'