# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import os

import pyvips
from pyvips import Image


# Make ImageMagick single threaded like other libraries are.
os.environ['VIPS_CONCURRENCY'] = '1'

pyvips.cache_set_max(0)
