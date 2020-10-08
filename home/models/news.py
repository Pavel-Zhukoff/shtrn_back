from django.db import models


class NewsModel(models.Model):

    name = models.CharField('Название', max_length=100)
    content = models.TextField('Описание')
    publish_date = models.DateTimeField('Дата и время публикации')
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField('Ссылка', unique=True)
    thumbnail = models.ImageField('Изображение новости', upload_to='news/%Y/%m/%d/')

    def get_absolute_url(self):
        return '/news/{}/'.format(self.slug)

    class Meta:
        db_table = 'news'
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
