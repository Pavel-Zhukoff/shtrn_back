from django.db import models

from .school import SchoolModel
from .subject import SubjectModel
from .teacher import TeacherModel
from .study_group import StudyGroupModel

class ScheduleModel(models.Model):

    WEEK = [
        (0, 'понедельник'),
        (1, 'вторник'),
        (2, 'среда'),
        (3, 'четверг'),
        (4, 'пятница'),
        (5, 'суббота'),
        (6, 'воскресенье'),
    ]

    weekday = models.CharField('День недели', max_length=1, choices=WEEK)
    start_time = models.TimeField('Время начала')
    end_time = models.TimeField('Время окончания')

    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, verbose_name='Преподаватель')
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE, verbose_name='Филиал', null=True)
    study_group = models.ForeignKey(StudyGroupModel, on_delete=models.CASCADE, verbose_name='Учебная группа', null=True)


    class Meta:

        db_table = 'schedule'
        verbose_name = 'расписание занятия'
        verbose_name_plural = 'расписнаия занятия'