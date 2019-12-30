import os

import pyvips
from pyvips import Image, Interpolate, at_least_libvips

from .base import BaseTestCase

# Make VIPS single threaded like other libraries are.
os.environ['VIPS_CONCURRENCY'] = '1'

pyvips.cache_set_max(0)


class VipsTestCase(BaseTestCase):
    @classmethod
    def resize(cls, im, *args, **kwargs):
        kernel = kwargs.pop('kernel', 'cubic')
        if at_least_libvips(8, 3):
            # resize with kernel added in 8.3
            kwargs['kernel'] = kernel
        else:
            kwargs['interpolate'] = Interpolate.new('bi' + kernel)

        return im.resize(*args, **kwargs)
