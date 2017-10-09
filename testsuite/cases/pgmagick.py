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

    def create_test_data(self):
        im = Image(root('resources', 'pineapple.jpeg').encode('utf-8'))
        if self.mode == 'RGB':
            im.type(ImageType.TrueColorType)
        elif self.mode == 'RGBA':
            pass
        elif self.mode == 'L':
            im.type(ImageType.GrayscaleType)
        elif self.mode in 'LA':
            im.type(ImageType.GrayscaleMatteType)
        else:
            raise ValueError('Unknown mode: {}'.format(self.mode))
        im.filterType(FilterTypes.CatromFilter)
        im.scale(Geometry(b"{}x{}!".format(self.size[0], self.size[1])))
        return [im]
