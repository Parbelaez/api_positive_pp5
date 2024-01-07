import logging

logger = logging.getLogger(__name__)

class LogResponseMiddleware:
    LOGIN_ENDPOINT = '/dj-rest-auth/login/'  # Update with your login endpoint

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if self.should_log(request.path):
            self.log_response(request, response)
        return response

    def should_log(self, path):
        return path == self.LOGIN_ENDPOINT

    def log_response(self, request, response):
        status_code = response.status_code
        method = request.method
        path = request.path
        headers = dict(response.items())

        logger.info(f"HTTP {method} {path} returned {status_code}")
        logger.info("Headers:")
        for header_name, header_value in headers.items():
            logger.info(f"  {header_name}: {header_value}")
            
    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     response = self.get_response(request)
    #     if request.path == '/dj-rest-auth/login/':
    #         logger.info(f"Response Body: {response.content}")
    #         logger.info(f"Response Headers: {dict(response.items())}")
    #     return response