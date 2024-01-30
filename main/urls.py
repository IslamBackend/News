from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as swagger_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/news/', include('news.urls')),
    path('api/v1/users/', include('users.urls')),
]
urlpatterns += swagger_urls
