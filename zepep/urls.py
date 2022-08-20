from django.contrib import admin
from django.urls import path, include

API_ROOT = 'api/v1/'

urlpatterns = [
    path(API_ROOT + 'admin/', admin.site.urls),
    path(API_ROOT, include('app.urls')),
]
