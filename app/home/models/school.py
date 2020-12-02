from django.db import models


class SchoolModel(models.Model):

    name = models.CharField('Навзвание филиала', max_length=150)
    address = models.CharField('Адрес', max_length=200)

    def __str__(self):
        return self.name

    class Meta:

        db_table = 'schools'
        verbose_name = 'филиал'
        verbose_name_plural = 'филиалы'