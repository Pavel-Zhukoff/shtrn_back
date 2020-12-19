from django.db import models


class TeacherModel(models.Model):

    name = models.CharField('Имя', max_length=100)
    job = models.CharField('Должность', max_length=250)
    experience = models.TextField('Стаж')
    education = models.TextField('Образование')
    photo = models.ImageField('Фото', upload_to=r'teachers/%Y/%m/%d/')
    sex = models.CharField('Пол', max_length=1, choices=(('f', 'Жен.'), ('m', 'Муж.'),), default='f')

    def __str__(self):
        return self.name

    class Meta:

        db_table = 'teachers'
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'
