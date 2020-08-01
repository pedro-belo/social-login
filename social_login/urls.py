from django.contrib import admin
from django.urls import path, include
from base import urls as base_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('', include(base_urls, namespace='base')),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('admin/', admin.site.urls),
]
