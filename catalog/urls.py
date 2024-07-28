from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, ProductListView, ProductDetailView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create')
]

# path("", home, name="home"),
# path("contacts/", contacts, name="contacts"),
