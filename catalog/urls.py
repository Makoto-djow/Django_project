from django.urls import path
from catalog.apps import CatalogConfig
# from catalog.views import home
# from catalog.views import contacts

from catalog.views import (ProductListView, ProductDetailView, contacts, BlogListView, BlogDetailView, BlogCreateView,
                           BlogUpdateView, BlogDeleteView)

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),

    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),

    path('', BlogListView.as_view(), name='blog_list'),
    path('products/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('products/create', BlogCreateView.as_view(), name='blog_create'),
    path('products/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('products/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),

]
