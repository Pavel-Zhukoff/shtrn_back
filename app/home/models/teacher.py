from django.db import models
import account.models


class TeacherModel(models.Model):

    job = models.CharField('Должность', max_length=250)
    experience = models.TextField('Стаж')
    education = models.TextField('Образование')
    photo = models.ImageField('Фото', upload_to=r'teachers/%Y/%m/%d/')

    user = models.OneToOneField(account.models.User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    class Meta:

        db_table = 'teachers'
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'
