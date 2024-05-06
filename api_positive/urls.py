from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# from .views import logout_route
# JWT Token Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    # Django REST Framework
    path('api/api-auth/', include('rest_framework.urls')),
    # dj-rest-auth for login and logout
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    # dj-rest-auth for registration
    path(
        'api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),

    # JWT Token Authentication
    path('api/dj-rest-auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('api/', include('profiles.urls')),
    path('api/', include('places.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('likes.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')
