from django.db import models
import account.models


class TeacherModel(models.Model):

    job = models.CharField('Должность', max_length=250)
    experience = models.TextField('Стаж')
    education = models.TextField('Образование')
    photo = models.ImageField('Фото', upload_to=r'teachers/%Y/%m/%d/')
    sex = models.CharField('Пол', max_length=1,
                           choices=(('f', 'Жен.'), ('m', 'Муж.'),),
                           default='f')
    user = models.OneToOneField(account.models.User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    @property
    def name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.get_full_name()


    class Meta:
        db_table = 'teachers'
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'