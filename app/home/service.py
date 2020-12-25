import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Value, F, Func
from django.db.models.functions import Concat

from account.models import GradeModel, User
from home.models import SchoolModel, SubjectModel, ScheduleModel, TeacherModel


def get_schedule():
    """ Возвращает расписание занятий по филиалам в json """
    answ = []
    for sch in SchoolModel.objects.all():
        school = {
            'name': sch.name,
            'grades': []
        }
        for grade in GradeModel.objects.all():
            grad = {
                'subjects': []
            }
            school['grades'].append(grad)
            for subj in SubjectModel.objects.filter(schedulemodel__school=sch, schedulemodel__study_group__classes=grade):
                subject = {
                    'name': subj.name,
                    'description': subj.description,
                    'schedule': {},
                }
                school['grades'][-1]['subjects'].append(subject)
                for w in range(7):
                    w = str(w)
                    school['grades'][-1]['subjects'][-1]['schedule'].update([(w, [])])
                    for sched in ScheduleModel.objects.filter(school=sch, subject=subj, weekday=w).order_by('start_time'):
                        schedule = {
                            'time': sched.start_time,
                            'group': sched.study_group.name
                        }
                        school['grades'][-1]['subjects'][-1]['schedule'][w].append(schedule)
        answ.append(school)
    return json.dumps(answ, cls=DjangoJSONEncoder)


def get_teachers():
    """ Возвращает json представление списка учителей """
    teachers = list(TeacherModel.objects
                    .annotate(name=Func(F('user__last_name'), Value(' '),
                                        F('user__first_name'), Value(' '),
                                        F('user__third_name'), function='CONCAT'))
                    .values('name', 'job', 'experience', 'education', 'photo', 'sex'))
    return json.dumps(teachers, cls=DjangoJSONEncoder)