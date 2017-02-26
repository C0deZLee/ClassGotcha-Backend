from classgotcha.settings.production import *

# Add tmp path
TMP_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, 'local/tmp'))

# Debug
DEBUG = TEMPLATES[0]['OPTIONS']['debug'] = True
#
# if 'debug_toolbar' not in INSTALLED_APPS:
#     INSTALLED_APPS += ('debug_toolbar',)

SECRET = '42'

# ------ Database ------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TMP_PATH, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ['127.0.0.1']


# -------- JWT AUTH --------
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,

    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=100),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=100),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# ----- Cross Origin Header -----
CORS_ORIGIN_WHITELIST = (
    'localhost:4000',
    '127.0.0.1:4000',
    'localhost:4004',
    '127.0.0.1:4004'
)

