# Generated by Django 3.1.2 on 2020-10-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_eventmodel_newsmodel_reviewmodel_subjectmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='students',
        ),
        migrations.DeleteModel(
            name='NewsModel',
        ),
        migrations.DeleteModel(
            name='SubjectModel',
        ),
        migrations.DeleteModel(
            name='EventModel',
        ),
    ]
