# Generated by Django 3.1.1 on 2020-09-24 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200922_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('third_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='Телефон')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'родитель',
                'verbose_name_plural': 'родители',
                'db_table': 'parents',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('third_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('school', models.CharField(max_length=100, verbose_name='Учебное заведение')),
                ('year_of_study', models.CharField(choices=[(1, 'первый'), (2, 'второй'), (3, 'третий'), (4, 'четвертый'), (5, 'пятый'), (6, 'шестой'), (7, 'седьмой'), (8, 'восьмой'), (9, 'девятый'), (10, 'десятый'), (11, 'одиннадцатый')], max_length=2, verbose_name='Год обучения')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.parentmodel', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'ученик',
                'verbose_name_plural': 'ученики',
                'db_table': 'students',
            },
        ),
    ]