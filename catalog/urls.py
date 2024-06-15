from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
# from catalog.views import home
# from catalog.views import contacts

from catalog.views import ProductListView, ProductDetailView, contacts, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),

    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),

]
