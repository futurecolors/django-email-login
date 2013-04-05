# coding: utf-8
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'email_login',
    'test_app'
)

SECRET_KEY = '_'
ROOT_URLCONF = 'test_app.urls'

STATIC_ROOT = '/var/www/localhost/htdocs/mysite/static/'
STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = ('email_login.auth_backend.EmailBackend',
                           'django.contrib.auth.backends.ModelBackend',)
