# -*- coding: utf-8 -*-
"""Django template tag that turns CSS blocks into style attributes using premailer."""
# :copyright: (c) 2016 Alex Hayes,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.
from __future__ import absolute_import, print_function, unicode_literals
from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info_t(0, 2, 0, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/django-premailer'
__docformat__ = 'restructuredtext'

# -eof meta-
