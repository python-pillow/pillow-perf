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

    def __init__(self, *args, **kwargs):
        self._free_resources = []
        super(WandTestCase, self).__init__(*args, **kwargs)

    def create_test_data(self, size, mode):
        im = Image(filename=root('resources', 'color_circle.png'))
        if mode == 'RGB':
            im.type = 'truecolor'
        elif mode == 'RGBA':
            pass
        elif mode == 'L':
            im.type = 'grayscale'
        elif mode in ('LA', 'La'):
            im.type = 'grayscalematte'
        else:
            raise ValueError('Unknown mode: {}'.format(mode))
        im.resize(size[0], size[1], 'catrom')
        self._free_resources.append(im)
        return [im]

    def __del__(self):
        for resource in self._free_resources:
            resource.destroy()
