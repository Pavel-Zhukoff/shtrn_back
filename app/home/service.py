import json

from home.models import SchoolModel, SubjectModel, ScheduleModel


def get_schedule():
    """ Возвращает расписание занятий по филиалам в json """
    answ = []
    for sch in SchoolModel.objects.all():
        school = {
            'name': sch.name,
            'subjects': []
        }
        for subj in SubjectModel.objects.filter(schedulemodel__school=sch):
            subject = {
                'name': subj.name,
                'description': subj.description,
                'schedule': [],
            }
            school['subjects'].append(subject)
            for w in range(7):
                school['subjects'][-1]['schedule'].update(str(w), [])
                for sched in ScheduleModel.objects.filter(school=sch, subject=subj, weekday=w).order_by('start_time'):
                    schedule = {
                        'time': sched.start_time,
                        'group': sched.study_group.name
                    }
                    school['subjects'][-1]['schedule'][w].append(schedule)
        answ.append(school)
    return json.dumps(answ)
