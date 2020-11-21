from django.shortcuts import render

from datetime import date

from account.models import ReviewModel
from home.models import TeacherModel, AdviceModel, TextbookModel, NewsModel, EventModel, SchoolModel, SubjectModel
from home.utils import get_referer_url, get_videos


def home(request):
    data = {
        'title': 'Главная',
        'news': NewsModel.objects.all(),
        'events': EventModel.objects.all(),
        'reviews': ReviewModel.objects.filter(is_moderated=True),
        'schools': SchoolModel.objects.all(),
        'subjects': SubjectModel.objects.all(),
        'year': date.today().year,
    }
    return render(request,
                  'home/schedule.html',
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