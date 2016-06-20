# -*- coding: utf-8 -*-
"""
    django_premailer.tests.settings
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Django test settings.
"""
from __future__ import absolute_import, print_function, unicode_literals
import os

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_premailer',
]

STATIC_URL = '/static/'

SECRET_KEY = 's3cr3t'

# Django replaces this, but it still wants it. *shrugs*
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE_CLASSES = {}

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(os.path.dirname(__file__), 'templates')
    ],
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
            'django.core.context_processors.tz',
            'django.core.context_processors.csrf',
            'django.contrib.messages.context_processors.messages',
            'django.core.context_processors.request',
        ]
    },
}]
