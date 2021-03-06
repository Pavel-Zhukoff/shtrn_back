# Generated by Django 3.1.2 on 2020-10-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20201012_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentmodel',
            options={'verbose_name': 'ученика', 'verbose_name_plural': 'ученики'},
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='school',
            field=models.CharField(max_length=100, verbose_name='Школа'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='year_of_study',
            field=models.IntegerField(choices=[(1, 'первый'), (2, 'второй'), (3, 'третий'), (4, 'четвертый'), (5, 'пятый'), (6, 'шестой'), (7, 'седьмой'), (8, 'восьмой'), (9, 'девятый'), (10, 'десятый'), (11, 'одиннадцатый')], max_length=2, verbose_name='Класс'),
        ),
    ]
