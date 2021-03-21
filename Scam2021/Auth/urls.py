from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('login/',views.index, name = 'index'),
    # path('login/',views.register, name = 'register'),
    path('loginauth/',views.login, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('home/', views.home, name = 'home'),
    path('FindMyDoc/', views.findDoc, name = 'finddoc'),
    path('Auth/chat/',views.chat, name = 'chat' ),
    path('Auth/booked/', views.booked, name = 'booked')
]