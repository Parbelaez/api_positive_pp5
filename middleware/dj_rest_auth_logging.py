import logging

logger = logging.getLogger(__name__)

class LogResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == '/dj-rest-auth/login/':
            logger.info(f"Response Body: {response.content}")
            logger.info(f"Response Headers: {dict(response.items())}")
        return response