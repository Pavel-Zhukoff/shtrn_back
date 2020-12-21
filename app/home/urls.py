from django.urls import path
from home.views import home, schedule_data, teachers, teachers_data


app_name = 'home'

urlpatterns = [
    path('', home, name='main-page'),
    path('schedule/data', schedule_data, name='schedule'),
    path('teachers', teachers, name='teachers'),
    path('teachers/data', teachers_data, name='teachers-data'),
]