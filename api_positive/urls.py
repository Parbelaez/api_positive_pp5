from django.contrib import admin
from django.urls import path, include
from .views import root_route
# JWT Token Authentication
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    # Django REST Framework
    path('api-auth/', include('rest_framework.urls')),
    # dj-rest-auth for login and logout
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # dj-rest-auth for registration
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),

    # JWT Token Authentication
    path('dj-rest-auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('profiles/', include('profiles.urls')),
    path('places/', include('places.urls')),
    path('posts/', include('posts.urls')),
    path('likes/', include('likes.urls')),
]
