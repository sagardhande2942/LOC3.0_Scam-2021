from django.urls import path
from .views import book, approve, find_doctor

urlpatterns = [
    path('book/<int:doctor_id>/', book),
    path('approve/', approve),
    path('find_doctor/', find_doctor)
]