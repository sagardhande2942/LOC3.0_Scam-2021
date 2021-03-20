from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('login/',views.register, name = 'register'),
    path('loginauth/',views.login, name = 'login'),
]