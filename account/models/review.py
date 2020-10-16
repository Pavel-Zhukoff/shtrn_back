from django.db import models


class ReviewModel(models.Model):

    text = models.TextField('Текст отзыва', blank=False)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    phone = models.CharField('Телефон', max_length=11)

    is_moderated = models.BooleanField('Проверено', default=False)

    def get_full_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    class Meta:

        db_table = 'reviews'
        verbose_name = 'отзыва'
        verbose_name_plural = 'отзывы'
