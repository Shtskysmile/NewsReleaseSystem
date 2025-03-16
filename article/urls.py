# article/urls.py
from django.urls import path

from user.urls import app_name
from . import views

app_name = 'article'
urlpatterns = [
    path('read/<int:aid>/', views.article_read, name='read'),
    path('edit/<int:aid>/', views.article_edit, name='edit'),
    path('delete/<int:aid>/', views.article_delete, name='delete'),
    path('write/', views.article_write, name='write'),
    path('list/', views.article_list, name='list'),
]