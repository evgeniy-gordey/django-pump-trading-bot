"""
Production Configurations

- Use mailgun to send emails
- Use Redis for cache


- Use Whitenoise for static

"""

import logging
from datetime import datetime, timedelta

from .base import *  # noqa

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env('DJANGO_SECRET_KEY')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Use Whitenoise to serve static files
# See: https://whitenoise.readthedocs.io/
WHITENOISE_MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE





# SITE CONFIGURATION
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[''])
DOMAIN = env('DJANGO_DOMAIN', default='https://github.com/eugordd/django-pump-trading-bot')

# Gunicorn
INSTALLED_APPS += ['gunicorn']




# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', default='django-pump-trading-bot <noreply@https://github.com/eugordd/django-pump-trading-bot>')
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[django-pump-trading-bot]')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# Anymail with Mailgun
INSTALLED_APPS += ['anymail']
ANYMAIL = {
    'MAILGUN_API_KEY': env('DJANGO_MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN')
}
EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

# Use the Heroku-style specification
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db('DATABASE_URL')

# CACHING
# ------------------------------------------------------------------------------

REDIS_URL = env('REDIS_URL', default='redis://127.0.0.1:6379')
REDIS_LOCATION = f'{REDIS_URL}/0'
# Heroku URL does not pass the DB number, so we parse it in
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_LOCATION,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    }
}


