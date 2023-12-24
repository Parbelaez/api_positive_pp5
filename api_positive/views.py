from rest_framework.decorators import api_view
from rest_framework.response import Response
# !dj-rest-auth bug fix workaround!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# from .settings import (
#     JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
#     JWT_AUTH_SECURE,
# )


@api_view()
def root_route(request):
    return Response({
        'message': 'Welcome to the Positive API',
        'version': '1.0.0',
        'author': 'Paulo Arbeláez',
        'Release': '20231224.1258',
    })