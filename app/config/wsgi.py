"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

import socketio
from django.core.wsgi import get_wsgi_application

from config import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

if settings.DEBUG:
    sio = socketio.Server(logger=True, ngineio_logger=True, cors_allowed_origins='*')
else:
    sio = socketio.Server(cors_allowed_origins='*')

application = socketio.WSGIApp(sio, get_wsgi_application())