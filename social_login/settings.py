from decouple import config, Csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'social_django',
    'rest_framework',
    'base',
    'todo'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    # Google
    'social_core.backends.google.GoogleOAuth2',

    # Facebook
    'social_core.backends.facebook.FacebookOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'social_login.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_login.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'base:user-area'
LOGOUT_REDIRECT_URL = 'account:login'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = config(
    'SOCIAL_AUTH_FACEBOOK_KEY')

SOCIAL_AUTH_FACEBOOK_SECRET = config(
    'SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to
# get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = config(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE', cast=Csv())


# Pipeline autenticação
SOCIAL_AUTH_DISCONNECT_PIPELINE = (

    # Caso o usuário não tenha senha,
    # envie-o para o form 'create-password'
    'account.pipeline.check_password',

    # Verifies that the social association
    # can be disconnected from the current
    # user (ensure that the user login mechanism
    # is not compromised by this
    # disconnection).
    'social_core.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social_core.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social_core.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social_core.pipeline.disconnect.disconnect',
)
