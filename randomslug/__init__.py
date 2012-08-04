import os
if 'DJANGO_SETTINGS_MODULE' in os.environ:
    from django.conf import settings
    settings.INSTALLED_APPS += ('randomslug.tests',)

VERSION = (0, 1, 3)

    