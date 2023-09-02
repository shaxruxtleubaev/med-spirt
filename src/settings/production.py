from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'farruxb1_mysql',
#         'USER': 'farruxb1_user',
#         'PASSWORD': 'gg1357908642',
#         'HOST': 'localhost',
#         'POST': '3306'
#     }
# }