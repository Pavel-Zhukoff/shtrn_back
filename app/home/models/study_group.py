from django.db import models

import account.models


class StudyGroupModel(models.Model):
    name = models.CharField('Название', max_length=100)

    classes = models.ManyToManyField(account.models.GradeModel, verbose_name='Классы')

    class Meta:
        db_table = 'study_groups'
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебной группы'