from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catalog',
        'USER': 'wins',
        'PASSWORD': 'wins',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
