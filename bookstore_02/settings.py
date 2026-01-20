from pathlib import Path
import os
from dotenv import load_dotenv

ENV_FILE = os.getenv("DJANGO_ENV_FILE", "env.dev")

load_dotenv(dotenv_path=ENV_FILE)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "e*1ralz5kdam3)_3w6o#*cse9bv9(i&-*)^py&9v(^!46w1c5&"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "debug_toolbar",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    # apps
    "product",
    "order",
    "home",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "bookstore_02.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookstore_02.wsgi.application"


# Database

# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("SQL_ENGINE", "django.db.backends.postgresql"),
#         "NAME": os.getenv("SQL_DATABASE", "bookstore_db"),
#         "USER": os.getenv("SQL_USER", "dev"),
#         "PASSWORD": os.getenv("SQL_PASSWORD", "dev"),
#         "HOST": os.getenv("SQL_HOST", "localhost"),
#         "PORT": os.getenv("SQL_PORT", "5432"),
#     }
# }
# retornando para o sqlite pois o pythonAnyere não tem suporte ao postgresql atual 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {  # Adiciona a "Paginação" do Django Rest Framework para os `ViewSets`
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEALT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

INTERNAL_IPS = [
    "127.0.0.1",
]

ALLOWED_HOSTS = ['costaanderson.pythonanywhere.com', 'localhost', '127.0.0.1']

DEBUG = os.getenv("DEBUG", "0") == "1"

CORS_ALLOWED_ORIGINS = [
    "https://CostaAnderson.pythonanywhere.com",
]

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"