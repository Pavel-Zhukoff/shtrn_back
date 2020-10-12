from django.db import models


class TextbookModel(models.Model):

    name = models.CharField('Название', max_length=150)
    file = models.FileField('Файл пособия', upload_to='textbooks/%Y/%m/%d/')

    class Meta:

        db_table = 'textbooks'
        verbose_name = 'учебное пособие'
        verbose_name_plural = 'учебные пособия'
