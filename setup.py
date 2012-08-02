from setuptools import setup, find_packages
import os

from randomslug import VERSION

setup(
    name = "django-randomslug",
    version = ".".join(map(str, VERSION)),
    packages = find_packages(),
    description = "reusable Django application providing the custom RandomSlugField model field",
    author = "Tvrtko Majstorovic",
    author_email = "tvrtkom@gmail.com",
    license = "MIT",
    url = 'http://github.com/TvrtkoM/django-randomslug',
)
