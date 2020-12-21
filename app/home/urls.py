from django.urls import path
from home.views import home, schedule, schedule_data, teachers, teachers_data


app_name = 'home'

urlpatterns = [
    path('', home, name='main-page'),
    path('schedule', schedule, name='schedule'),
    path('schedule/data', schedule_data, name='schedule-data'),
    path('teachers', teachers, name='teachers'),
    path('teachers/data', teachers_data, name='teachers-data'),
]