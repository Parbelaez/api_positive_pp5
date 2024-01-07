from pathlib import Path
import os
import re
import dj_database_url

if os.path.exists('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEBUG' in os.environ

ALLOWED_HOSTS = [
    'localhost',
    '.gitpod.io',
    '.herokuapp.com',
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "https://*.gitpod.io",
    "https://*.herokuapp.com",
]

# Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',

    # Django REST Framework
    'rest_framework',
    'rest_framework.authtoken',  # Django REST Framework Token Authentication
    'dj_rest_auth',
    # Registration
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    # CORS
    'corsheaders',

    # Apps
    'profiles',
    'places',
    'posts',
    'likes',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # ... custom middleware ...
    'middleware.dj_rest_auth_logging.LogResponseMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'api_positive.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api_positive.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# If DEV is set to True, use sqlite3, else use postgres
if 'DEV_DB' in os.environ and os.environ.get('DEV_DB') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    # The line will be left commented to test the DB connection
    print('connected to postgres')

# Django REST Framework

REST_FRAMEWORK = {
    # Pagination
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    # Date and time formats
    'DATETIME_FORMAT': "%Y-%m-%d at %-I:%M %p",
}


# Authentication: JWT in production, Session in development
if 'SESS_AUTH' in os.environ:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
            'rest_framework.authentication.SessionAuthentication',
        ]
    print('using session auth')
else:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
    print('using jwt')

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_SECURE': True,
    'JWT_AUTH_COOKIE': 'positive-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'positive-refresh-token',
    # When this flag is set to false, the refresh token will be sent in the body
    # Unless, it will be only in a cookie
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_SAMESITE': 'LAX',
    'JWT_AUTH_COOKIE_DOMAIN' : '.gitpod.io',
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'api_positive.serializers.CurrentUserSerializer'
}

# CORS Configuration

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
    print(os.environ.get('CLIENT_ORIGIN'))

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(
        r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE
    ).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
    print(os.environ.get('CLIENT_ORIGIN_DEV'))

CORS_ALLOW_CREDENTIALS = True

# We need to disable the email verification in order to be able to create users from the API
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False

# JSON and html renderer only in development
if 'HTML_REND' not in os.environ or os.environ.get('HTML_REND') != 'True':
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
            'rest_framework.renderers.JSONRenderer',
        ]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

print(REST_FRAMEWORK)