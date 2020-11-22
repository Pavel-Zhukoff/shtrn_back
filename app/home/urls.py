from django.urls import path
from home.views import home, schedule


app_name = 'home'

urlpatterns = [
    path('', home, name='main-page'),
    path('schedule', schedule, name='schedule'),
]