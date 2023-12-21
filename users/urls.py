from django.urls import path, include
from users.views import personal_account, register, user_login, user_logout

urlpatterns = [
    path('', personal_account, name='account'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
