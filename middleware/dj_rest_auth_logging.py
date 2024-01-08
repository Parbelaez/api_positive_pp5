import logging

logger = logging.getLogger(__name__)

class LogResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        body = response.content
        headers = dict(response.items())
        connection: respnse.get(connection, alternate=None)
        content_length = response.get(content-length, alternate=None)
        if request.path == '/dj-rest-auth/login/':
            logger.info("Headers:")
            for header_name, header_value in headers.items():
                logger.info(f"  {header_name}: {header_value}")
            logger.info(f"Connection:  {connection}")
            logger.info(f"Response Body: {body}")
        set_cookie_headers = response.get_all('Set-Cookie')
        if set_cookie_headers:
            logger.info("Set-Cookie headers:")
            for set_cookie_header in set_cookie_headers:
                logger.info(f"  {set_cookie_header}")

        return response