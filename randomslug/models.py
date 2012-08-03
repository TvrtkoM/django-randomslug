from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode
import random

import validators
import app_settings

def slugify(value, i=None):
    random.seed()
    slug = default_slugify(value)
    if i is not None:
        slug += "_%d" % i
    return slug

class RandomSlugField(models.Field):
    description = _("Unique Slug")
    
    def __init__(self, slug_length=10, *args, **kwargs):
        kwargs['editable'] = False
        self.slug_length = slug_length
        if 'db_index' not in kwargs:
            kwargs['db_index'] = True
        super(RandomSlugField, self).__init__(*args, **kwargs)
        self.validators.append(validators.RandomSlugLengthValidator(self.slug_length))
    
    def db_type(self, connection):
        return 'varchar'

    def get_internal_type(self):
        return "UniqueSlugField"
    
    def to_python(self, value):
        return smart_unicode(value)
    
    def get_prep_value(self, value):
        return self.to_python(value)
    
    def pre_save(self, model_instance, add):
        if add is True:
            value = "".join(random.choice(app_settings.SLUG_CHARACTERS) for x in range(self.slug_length))
            slug = slugify(value)
            model_cls = model_instance.__class__
            i = 1
            while True:
                try:
                    model_cls.objects.get(**{self.attname: slug})
                except model_cls.DoesNotExist:
                    setattr(model_instance, self.attname, slug)
                    return slug
                slug = slugify(value, i)
                i += 1
        else:
            return super(RandomSlugField, self).pre_save(model_instance, add)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^randomslug\.models\.RandomSlugField"])
