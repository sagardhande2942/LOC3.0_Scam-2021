
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Auth.urls')),
    path('appointment/', include('Appointments.urls'))
]
