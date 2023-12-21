from django.contrib import admin
from django.urls import path, include
from .views import root_route


urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
