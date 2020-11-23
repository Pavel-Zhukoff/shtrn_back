from django.urls import path
from home.views import home, schedule_data


app_name = 'home'

urlpatterns = [
    path('', home, name='main-page'),
    path('schedule/data', schedule_data, name='schedule'),
]