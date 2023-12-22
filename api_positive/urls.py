from django.contrib import admin
from django.urls import path, include
from .views import root_route


urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Django REST Framework
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # dj-rest-auth
]
