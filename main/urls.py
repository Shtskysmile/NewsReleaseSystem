from django.urls import path
from . import views

app_name = 'main'  # 定义一个命名空间
urlpatterns = [
    path('', views.index, name='index'),
]
