from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('base.urls', namespace='base')),
    path('account/', include('account.urls', namespace='account')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
