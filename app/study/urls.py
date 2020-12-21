from django.urls import path

from study.views import room

app_name = 'study'

urlpatterns = [
    path('room/<slug:room_slug>', room, name='room'),
]