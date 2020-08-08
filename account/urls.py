from django.contrib.auth import views as auth_views
from account import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreationView.as_view(), name='register'),
    path('settings/', views.settings, name='settings'),
    path('create-password/', views.CreatePasswordView.as_view(),
         name='create-password')
]
