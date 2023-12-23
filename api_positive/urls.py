from django.contrib import admin
from django.urls import path, include
from .views import root_route
# JWT Token Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Django REST Framework
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # dj-rest-auth

    # JWT Token Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('profiles/', include('profiles.urls')),
]
