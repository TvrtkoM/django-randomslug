from django.db import models

from randomslug.models import *

class Slug(models.Model):
    slug = RandomSlugField()
