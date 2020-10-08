from django.db import models


class TeacherModel(models.Model):

    name = models.CharField('Название', max_length=100)
    job = models.CharField('Должность', max_length=250)
    experience = models.TextField('Стаж')
    education = models.TextField('Образование')
    photo = models.ImageField('Фото', upload_to=r'teachers/%Y/%m/%d/')

    class Meta:

        db_table = 'teachers'
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'