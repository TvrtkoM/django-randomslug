from django.conf import settings
import re

# characters to use to generate a slug
SLUG_CHARACTERS = getattr(settings, 'RANDOMSLUG_CHARACTERS', 
                          'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890')

# if SLUG_CHARACTERS consists of characters other than alphanumeric, hyphen or underscore,
# ValueError exception is raised
invalid_characters = re.search(r'[^a-z^A-Z^0-9^_^-]+', SLUG_CHARACTERS)
if invalid_characters is not None:
    raise ValueError('RANDOMSLUG_CHARACTERS setting has invalid characters %s' % invalid_characters.group())
