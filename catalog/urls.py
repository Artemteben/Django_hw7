from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, base_r, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', base_r, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]

# path("", home, name="home"),
# path("contacts/", contacts, name="contacts"),
