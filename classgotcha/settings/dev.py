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

# ------ Account customization ------

ACCOUNT_USER_DISPLAY = lambda user: user.email
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

TEST_RUNNER = "lib.tests.MyTestDiscoverRunner"

# ------ REST Framework ------
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
