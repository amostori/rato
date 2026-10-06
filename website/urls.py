from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('category/<int:category_id>', views.posts_by_category, name='posts_by_category'),
    path('blog/<slug:slug>', views.blog, name='blog'),
    path('search/', views.search, name='search'),
]