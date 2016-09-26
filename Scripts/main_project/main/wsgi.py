"""
WSGI config for main_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
