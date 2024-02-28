from django.urls import path
from user.views import *

urls = [
   path('login/',login,name='login'),
   path('register/',register,name ='register')
]