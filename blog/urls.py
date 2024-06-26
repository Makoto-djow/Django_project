from django.urls import path
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [

    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create', BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),

]
