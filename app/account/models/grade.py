from django.db import models


class GradeModel(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        db_table = 'grades'
        verbose_name = 'класс'
        verbose_name_plural = 'класса'