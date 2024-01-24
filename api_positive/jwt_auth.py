from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions, serializers
from dj_rest_auth import jwt_auth
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

class CustomCookieAuthentication(jwt_auth.JWTCookieAuthentication):
    """
    An authentication plugin that hopefully authenticates requests through a JSON web
    token provided in a request cookie (and through the header as normal, with a
    preference to the header).
    """

    def authenticate(self, request):
        cookie_name = settings.JWT_AUTH_COOKIE
        logger.info(f"Auth Cookie Name:  {cookie_name}")
        header = self.get_header(request)
        logger.info(f"Header:  {header}")
        if header is None:
            if cookie_name:
                raw_token = request.COOKIES.get(cookie_name)
                logger.info(f"Raw Token:  {raw_token}")
            else:
                return None
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        logger.info(f"Validated Token :  {validated_token}")
        return self.get_user(validated_token), validated_token