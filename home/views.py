from django.shortcuts import render

from datetime import date

from home.models import TeacherModel, AdviceModel, TextbookModel
from home.utils import get_referer_url, get_videos


def home(request):
    data = {}
    return render(request,
                  'home/index.jhtml',
                  data)


def teachers(request):
    data = {
        'title': 'Преподаватели',
        'teachers': TeacherModel.objects.all(),
        'prev': get_referer_url(request),
        'year': date.today().year,
        }
    return render(request,
                  'home/teachers.jhtml',
                  data)

def schedule(request):
    pass

def high_school(request):
    data = {
        'title': 'Старшая школа',
        'advices': AdviceModel.objects.all(),
        'videos': get_videos(),
        'textbooks': TextbookModel.objects.all(),
        'prev': get_referer_url(request),
        'year': date.today().year,
    }
    return render(request,
                  'home/high_school.jhtml',
                  data)