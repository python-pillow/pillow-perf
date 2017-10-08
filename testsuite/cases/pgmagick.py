# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import os

# Make GraphicsMagick single threaded like other libraries are.
os.environ['OMP_NUM_THREADS'] = '1'


from pgmagick import Image, FilterTypes, ImageType, Geometry

from .base import BaseTestCase, root


class PgmagickTestCase(BaseTestCase):
    filter_ids = {
        FilterTypes.LanczosFilter: 'lzs',
        FilterTypes.TriangleFilter: 'bil',
        FilterTypes.CatromFilter: 'bic',
        FilterTypes.HammingFilter: 'hmn',
        FilterTypes.BoxFilter: 'box',
    }

    def create_test_data(self, size, mode):
        im = Image(root('resources', 'color_circle.png').encode('utf-8'))
        if mode == 'RGB':
            im.type(ImageType.TrueColorType)
        elif mode == 'RGBA':
            pass
        elif mode == 'L':
            im.type(ImageType.GrayscaleType)
        elif mode in 'LA':
            im.type(ImageType.GrayscaleMatteType)
        else:
            raise ValueError('Unknown mode: {}'.format(mode))
        im.filterType(FilterTypes.CatromFilter)
        im.scale(Geometry(b"{}x{}!".format(size[0], size[1])))
        return [im]
