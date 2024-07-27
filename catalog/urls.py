from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, base_r

app_name = CatalogConfig.name

urlpatterns = [path('', base_r, name='product_list')]
# path("", home, name="home"),
# path("contacts/", contacts, name="contacts"),
