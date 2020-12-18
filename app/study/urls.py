from django.urls import path

app_name = 'study'

urlpatterns = [
    path('room/<slug:room_slug>', lambda x: x, name='room'),
]