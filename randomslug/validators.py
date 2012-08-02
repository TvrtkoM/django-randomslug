from django.core.validators import BaseValidator
from django.utils.translation import ugettext_lazy as _
import re

import app_settings

def sluglen(slug, characters):
    """return the length of a slug consisting only of specified characters
    
    arguments:
    slug -- a slug string
    characters -- a string of characters that slug consists of
    
    """
    pattern = r'^(?P<slug>[' + characters + ']+)(_\d+)?$'
    res = re.match(pattern, slug)
    if res is not None:
        return len(res.groupdict()['slug'])
    else:
        return 0

class RandomSlugLengthValidator(BaseValidator):
    compare = lambda self, a, b: a != b
    clean = lambda self, x: sluglen(x, app_settings.SLUG_CHARACTERS)
    message = _(u'Ensure this value has exactly %(limit_value)d characters (it is %(show_value)d).')
    code = 'slug_length'