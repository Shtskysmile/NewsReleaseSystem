from django.urls import path
from . import views

app_name = 'user'  # 定义一个命名空间
urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]
