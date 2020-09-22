from django.urls import path

from account.views import register, code_verification, personal_page, login


app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('verify/', code_verification, name='code_verification'),
    path('login/', login, name='login'),
    path('', personal_page, name='main-page')
]