import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

STATIC_DIR = BASE_DIR.parent

sys.path.append((BASE_DIR / 'apps').as_posix())

SECRET_KEY = 'django-insecure-=sa$$6qy4*#ocb-guco9k%ko6yrt42kauub+7nc53t)lc1w6!6'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # --------- Django ---------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # --------- Libs ---------
    'rest_framework',
    'rest_framework_swagger',
    'django_filters',
    'djoser',
    'corsheaders',
    'versatileimagefield',
    'constance',
    'constance.backends.database',
    'ckeditor',
    # --------- Local ---------
    'apps.users.apps.UsersConfig',
    'apps.posts.apps.PostsConfig',
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

ROOT_URLCONF = 'project_config.urls'

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

            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'project_config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = STATIC_DIR / 'static/'
MEDIA_ROOT = STATIC_DIR / 'media/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        'rest_framework.authentication.SessionAuthentication',
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

AUTH_USER_MODEL = 'users.User'

# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono',
#         # 'skin': 'office2013',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         'toolbar_YourCustomToolbarConfig': [
#             {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             '/',
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['About']},
#             '/',  # put this to force next toolbar on new line
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',
#
#             ]},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
#         # 'height': 291,
#         # 'width': '100%',
#         # 'filebrowserWindowHeight': 725,
#         # 'filebrowserWindowWidth': 940,
#         # 'toolbarCanCollapse': True,
#         # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'LANGUAGE': ('EN', 'Select language', 'language_select'),
}

CONSTANCE_ADDITIONAL_FIELDS = {
    'language_select': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': (('EN', 'English'), ('RU', 'Русский'))
    }]
}
