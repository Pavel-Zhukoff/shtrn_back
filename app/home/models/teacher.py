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

    user = models.OneToOneField(account.models.User, on_delete=models.RESTRICT, verbose_name='Пользователь')

    @property
    def first_name(self):
        return self.user.first_name

    @first_name.setter
    def first_name(self, value):
        self.user.first_name = str(value).strip().capitalize()

    @property
    def last_name(self):
        return self.user.last_name

    @last_name.setter
    def last_name(self, value):
        self.user.last_name = str(value).strip().capitalize()

    @property
    def third_name(self):
        return self.user.third_name

    @third_name.setter
    def third_name(self, value):
        self.user.third_name = str(value).strip().capitalize()

    def get_full_name(self):
        return self.user.get_full_name()

    def get_short_name(self):
        return self.user.get_short_name()

    @property
    def name(self):
        return self.get_full_name()


    class Meta:
        db_table = 'teachers'
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'