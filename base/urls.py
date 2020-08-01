from django.contrib.auth import views as auth_views
from django.urls import path, include
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user_area, name='user-area')
]