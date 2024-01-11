from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'message': 'Welcome to the Positive API',
        'version': '1.2.1',
        'author': 'Paulo Arbeláez',
        'Release': '20240111.22.20_m',
    })