from django_project.settings import *

globals().setdefault('DEBUG', False)

if DEBUG:
   INSTALLED_APPS += [
      'django_extensions',
      'debug_toolbar',
   ]

   MIDDLEWARE += [
      'debug_toolbar.middleware.DebugToolbarMiddleware',
   ]

   INTERNAL_IPS = [
      '127.0.0.1',
   ]
