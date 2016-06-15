"""Default Django settings."""
import os


here = os.path.dirname(os.path.abspath(__file__))
package_dir = os.path.dirname(here)


# Default paths depend on sys.platform.
DATA_DIR = os.path.join('/', 'var', 'lib', 'minventoryapi')

DEBUG = False
ALLOWED_HOSTS = []


# Application definition. Ordering matters: first overrides last.
INSTALLED_APPS = [
    # Specific stuff for project.
    'minventoryapi.inventory',
    # Third-parties.
    'rest_framework',
    'rest_framework_swagger',
    # Django builtins.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Things that MUST be at the end.
    'debug_toolbar',
]
MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]


ROOT_URLCONF = 'minventoryapi.urls'
USE_X_FORWARDED_HOST = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'minventoryapi.wsgi.application'


# Databases MUST BE customized in local settings.
DATABASES = {}


# Internationalization
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'fr'
USE_TZ = True
TIME_ZONE = 'Europe/Paris'


# Auth.


# Static files (CSS, JavaScript, Images)
# STATIC_URL and MEDIA_URL depend on reverse proxy configuration, so they need
# to be defined in local settings.
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')


# REST framework.
REST_FRAMEWORK = {
    'VIEW_DESCRIPTION_FUNCTION':
        'rest_framework_swagger.views.get_restructuredtext',
}
SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '0.1',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'doc_expansion': 'none',
}
