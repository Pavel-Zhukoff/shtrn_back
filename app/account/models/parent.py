from django.db import models


class ParentModel(models.Model):
    first_name = models.CharField('Имя', max_length=30, null=True)
    last_name = models.CharField('Фамилия', max_length=30, null=True)
    third_name = models.CharField('Отчество', max_length=30, null=True, blank=True, default='')
    phone = models.CharField('Телефон', max_length=11)

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.third_name)

    get_full_name.short_description = 'ФИО'
    get_full_name.admin_order_field = 'last_name'

    def get_short_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    get_short_name.short_description = 'Имя'


    def sms_user(self, message):
        send_sms(self.phone, message)
