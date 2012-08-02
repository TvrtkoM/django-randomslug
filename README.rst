Django RandomSlugField
======================

A simple model field providing random & unique slug field for your django models

Installation
------------
::

    python setup.py install
    
Append 'randomslug' to your INSTALLED_APPS setting

Usage
-----

Create a django model like usual and add a RandomSlugField::

    # models.py
    from randomslug.models import RandomSlugField
    
    class ModelWithSlug(models.Model):
        slug = RandomSlugField()


The slug value will now be randomized each when the model has to be saved to database
for the first time. If the same value already exist the value will get suffix of the 
pattern "_%d" % number where number is positive integer, so each slug will be unique.

RandomSlugField accepts slug_length option which represents the number of randomized
characters in slug (excluding number suffix) e.g. slugs 'xc-45' & 'xf987_23'
are both of the slug_length 5
