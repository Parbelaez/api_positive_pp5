import logging

logger = logging.getLogger(__name__)

class LogResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        body = response.content
        headers = dict(response.items())
        if request.path == '/dj-rest-auth/login/':
            logger.info(response)
            logger.info(f"Response Body: {body}")
            logger.info("Headers:")
            for header_name, header_value in headers.items():
                logger.info(f"  {header_name}: {header_value}")
        return response