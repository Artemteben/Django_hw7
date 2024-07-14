from django.contrib import admin
from django.urls import path, include

import catalog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
]
