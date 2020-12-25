from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def personal_page(request):
    return HttpResponse('<h1>Личный кабинет пользователя с телеоном {}</h1>'.format(request.user.phone))