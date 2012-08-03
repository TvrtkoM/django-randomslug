"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.db import models
import re

from randomslug.models import *
from randomslug.validators import sluglen

from .models import Slug

class SluglenTest(TestCase):
    def setUp(self):
        self.default = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
        self.custom = '-gda985'

    def test_valid_slugs_default_characters(self):
        valids = ['xCodJFRc', '1fGkb_2234', 'dfsNFDe_1', '023BBDf']
        for slug in valids:
            self.assertNotEqual(sluglen(slug, self.default), 0)
        self.assertEqual(sluglen(valids[0], self.default), 8)
        self.assertEqual(sluglen(valids[1], self.default), 5)
        self.assertEqual(sluglen(valids[2], self.default), 7)
        self.assertEqual(sluglen(valids[3], self.default), 7)
        
    def test_invalid_slugs_default_characters(self):
        invalids = ['xC_odJFRc', '1&&&fGkb_2234', '_dfsNFDe_1', '%023BBDf']
        for slug in invalids:
            self.assertEqual(sluglen(slug, self.default), 0)

    def test_valid_slugs_custom_characters(self):
        valids = ['gda985_12', '95-_3', 'ga-9_9999']
        for slug in valids:
            self.assertNotEqual(sluglen(slug, self.custom), 0)
        self.assertEqual(sluglen(valids[0], self.custom), 6)
        self.assertEqual(sluglen(valids[1], self.custom), 3)
        self.assertEqual(sluglen(valids[2], self.custom), 4)
        
    def test_invalid_slugs_custom_characters(self):
        invalids = ['gcda985_12', '4495-_3', 'ga-33239_9999']
        for slug in invalids:
            self.assertEqual(sluglen(slug, self.custom), 0)

class SlugifyTest(TestCase):
    def setUp(self):
        self.default = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
        self.value = "".join(random.choice(self.default) for x in range(10))
        self.pattern = r'^(?P<slug>[' + self.default + ']+)(_\d+)?$'

    def test_generated_slug_length(self):
        slug = slugify(self.value)
        self.assertEqual(sluglen(slug, self.default), 10)
        slug = slugify(self.value, 4)
        self.assertEqual(sluglen(slug, self.default), 10)
        
    def test_generated_slug_pattern(self):
        slug = slugify(self.value)
        self.assertNotEqual(re.match(self.pattern, slug), None)

class RandomSlugFieldTest(TestCase):
    def setUp(self):
        self.default = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
        self.pattern = r'^(?P<slug>[' + self.default + ']+)(_\d+)?$'

    def test_slug_length(self):
        slugfield = RandomSlugField(10)
        self.assertEqual(slugfield.slug_length, 10)
        
    def test_slug_in_model(self):
        slugmodel = Slug()
        self.assertEqual(slugmodel.slug, u'')
        slugmodel.save()
        self.assertIsNotNone(slugmodel.slug)
        self.assertEqual(sluglen(slugmodel.slug, self.default), 10)
        self.assertIsNotNone(re.match(self.pattern, slugmodel.slug))
        
    def test_slug_db_type(self):
        slugfield = RandomSlugField()
        self.assertEqual(slugfield.db_type(None), 'varchar(10)')
        slugfield = RandomSlugField(5)
        self.assertEqual(slugfield.db_type(None), 'varchar(5)')
