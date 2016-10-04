from classgotcha.settings.production import *

# Add tmp path
TMP_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, 'local/tmp'))

# Debug
DEBUG = TEMPLATES[0]['OPTIONS']['debug'] = True

if 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS += ('debug_toolbar',)


SECRET = '42'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TMP_PATH, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ['127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'