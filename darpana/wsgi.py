"""
WSGI config for darpana project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from subprocess import call

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "darpana.settings")

# Execute the build script to copy template into the right dir
call(["sh", "build.sh"])

application = get_wsgi_application()
