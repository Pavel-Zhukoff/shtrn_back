from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

from account.models import ReviewModel
from home.models import TeacherModel, AdviceModel, TextbookModel, NewsModel, EventModel, SchoolModel, SubjectModel
from home.utils import get_referer_url, get_videos
from home.service import get_schedule, get_teachers


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
                  'home/teachers.html',
                  data)


def teachers(request):
    data = {
        'title': 'Преподаватели',
        'prev': get_referer_url(request),
        'year': date.today().year,
        }
    return render(request,
                  'home/teachers.html',
                  data)


def schedule(request):
    data = {
        'title': 'Расписание',
        'prev': get_referer_url(request),
        'year': date.today().year,
        }
    return render(request,
                  'home/schedule.html',
                  data)


def teachers_data(request):
    return HttpResponse(get_teachers())


def schedule_data(request):
    return HttpResponse(get_schedule())


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
