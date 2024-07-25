from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, index

app_name = CatalogConfig.name

urlpatterns = [path('', index)]
# path("", home, name="home"),
# path("contacts/", contacts, name="contacts"),
