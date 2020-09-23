from django.urls import path

from account.views import register, code_verification, personal_page, login, password_change, logout

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('verify/', code_verification, name='code_verification'),
    path('login/', login, name='login'),
    path('password/', password_change, name='password_change'),
    path('logout/', logout, name='logout'),
    path('', personal_page, name='main-page')
]