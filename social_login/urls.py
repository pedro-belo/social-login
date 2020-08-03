from django.contrib import admin
from django.urls import path, include
from base import urls as base_urls
from todo import urls as todo_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('', include(base_urls, namespace='base')),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('todo/', include(todo_urls, namespace='todo')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]