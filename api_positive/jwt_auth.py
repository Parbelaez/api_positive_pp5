from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions, serializers
from dj_rest_auth import jwt_auth
import logging


logger = logging.getLogger(__name__)

class CustomCookieAuthentication(jwt_auth.JWTCookieAuthentication):
    """
    An authentication plugin that hopefully authenticates requests through a JSON web
    token provided in a request cookie (and through the header as normal, with a
    preference to the header).
    """
    logger.info("JWT Custon Auth")
    def enforce_csrf(self, request):
        """
        Enforce CSRF validation for session based authentication.
        """
        def dummy_get_response(request):  # pragma: no cover
            return None
        check = CSRFCheck(dummy_get_response)
        logger.info(f"check:  {check}")
        # populates request.META['CSRF_COOKIE'], which is used in process_view()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        logger.info(f"Reason:  {reason}")
        if reason:
            # CSRF failed, bail with explicit error message
            raise exceptions.PermissionDenied(f'CSRF Failed: {reason}')

    def authenticate(self, request):
        cookie_name = api_settings.JWT_AUTH_COOKIE
        logger.info(f"Auth Cookie Name:  {cookie_name}")
        header = self.get_header(request)
        logger.info(f"Header:  {header}")
        if header is None:
            if cookie_name:
                raw_token = request.COOKIES.get(cookie_name)
                logger.info(f"Raw Token:  {raw_tokem}")
                if api_settings.JWT_AUTH_COOKIE_ENFORCE_CSRF_ON_UNAUTHENTICATED: #True at your own risk
                    self.enforce_csrf(request)
                elif raw_token is not None and api_settings.JWT_AUTH_COOKIE_USE_CSRF:
                    self.enforce_csrf(request)
            else:
                return None
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        logger.info(f"Validated Token :  {validated_token}")
        return self.get_user(validated_token), validated_token