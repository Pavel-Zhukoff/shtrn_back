import json

from django.core.serializers.json import DjangoJSONEncoder

from account.models import GradeModel
from home.models import SchoolModel, SubjectModel, ScheduleModel


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
