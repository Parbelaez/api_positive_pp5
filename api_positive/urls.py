from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# from .views import root_route
# JWT Token Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('', root_route),
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
    # Apps
    path('api/profiles/', include('profiles.urls')),
    path('api/places/', include('places.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/likes/', include('likes.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')
