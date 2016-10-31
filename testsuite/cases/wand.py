# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import os

from wand.image import Image

from .base import BaseTestCase, root


# Make ImageMagick single threaded like other libraries are.
os.environ['MAGICK_THREAD_LIMIT'] = '1'


class WandTestCase(BaseTestCase):
    filter_ids = {
        'lanczos': 'lzs', 'triangle': 'bil', 'catrom': 'bic', 'hamming': 'hmn',
    }

    def create_test_data(self, size, mode):
        im = Image(filename=root('resources', 'color_circle.png'))
        if mode == 'RGB':
            im.type = 'truecolor'
        elif mode == 'L':
            im.type = 'grayscale'
        elif mode in ('LA', 'La'):
            im.type = 'grayscalematte'
        else:
            raise ValueError('Unknown mode: {}'.format(mode))
        im.resize(size[0], size[1], 'catrom')
        return [im]
