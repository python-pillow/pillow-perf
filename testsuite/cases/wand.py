# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import os
import ctypes
import numbers

from wand.image import Image, manipulative
from wand.api import library

from .base import BaseTestCase, root


# Make ImageMagick single threaded like other libraries are.
os.environ['MAGICK_THREAD_LIMIT'] = '1'

library.MagickBlurImage.argtypes = [ctypes.c_void_p,
                                    ctypes.c_double,
                                    ctypes.c_double]


class WandTestCase(BaseTestCase):
    filter_ids = {
        'lanczos': 'lzs', 'triangle': 'bil', 'catrom': 'bic', 'hamming': 'hmn',
    }

    def __init__(self, *args, **kwargs):
        self._free_resources = []
        super(WandTestCase, self).__init__(*args, **kwargs)

    def create_test_data(self):
        im = Image(filename=root('resources', 'color_circle.png'))
        if self.mode == 'RGB':
            im.type = 'truecolor'
        elif self.mode == 'RGBA':
            im.type = 'truecolormatte'
        elif self.mode == 'L':
            im.type = 'grayscale'
        elif self.mode in 'LA':
            im.type = 'grayscalematte'
        else:
            raise ValueError('Unknown mode: {}'.format(self.mode))
        im.resize(self.size[0], self.size[1], 'catrom')
        self._free_resources.append(im)
        return [im]

    def __del__(self):
        for resource in self._free_resources:
            resource.destroy()

    @staticmethod
    @manipulative
    def blur(self, radius, sigma):
        if not isinstance(radius, numbers.Real):
            raise TypeError('radius has to be a numbers.Real, not ' +
                            repr(radius))
        elif not isinstance(sigma, numbers.Real):
            raise TypeError('sigma has to be a numbers.Real, not ' +
                            repr(sigma))
        r = library.MagickBlurImage(self.wand, radius, sigma)
        if not r:
            self.raise_exception()
