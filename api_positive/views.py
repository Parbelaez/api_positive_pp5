from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'message': 'Welcome to the Positive API',
        'version': '1.1.1',
        'author': 'Paulo Arbeláez',
        'Release': '20240110.21.51_m',
    })