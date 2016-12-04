# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import math

from PIL import Image

from .base import BaseTestCase, root


Image.LANCZOS = Image.ANTIALIAS


class PillowTestCase(BaseTestCase):
    filter_ids = {
        0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        4: 'box', 5: 'hmn', 6: 'mtc',
    }

    def create_test_data(self, size, mode):
        im = Image.open(root('resources', 'color_circle.png'))
        im = im.convert(mode)
        im = self.resize(im, size, Image.BICUBIC)
        return [im]

    @classmethod
    def resize(cls, self, size, resample=Image.NEAREST):
        self.load()

        if self.size == size:
            return self._new(self.im)

        if self.mode in ("1", "P"):
            resample = Image.NEAREST

        if self.mode == 'RGBA':
            return cls.resize(self.convert('RGBa'),
                              size, resample).convert('RGBA')

        if self.mode == 'LA':
            return cls.resize(self.convert('La'),
                              size, resample).convert('LA')

        if resample == Image.NEAREST or not hasattr(self.im, 'stretch'):
            im = self.im.resize(size, resample)
        else:
            im = self.im.stretch(size, resample)

        return self._new(im)

    @classmethod
    def gaussian_blur(cls, self, radius, n=3):
        if self.mode == 'RGBA':
            return cls.gaussian_blur(self.convert('RGBa'),
                                     radius, n).convert('RGBA')

        if self.mode == 'LA':
            return cls.gaussian_blur(self.convert('La'),
                                     radius, n).convert('LA')

        # http://www.mia.uni-saarland.de/Publications/gwosdek-ssvm11.pdf
        # [7] Box length.
        L = math.sqrt(12.0 * float(radius) * radius / n + 1.0)
        # [11] Box radius.
        l = (L - 1.0) / 2.0
        # Integer part.
        li = math.floor(l)
        # Reduce the fractional part in accordance with tests.
        a = math.e ** (2.5 * (l - li) / (li + 1)) - 1
        a /= math.e ** (2.5 / (li + 1)) - 1
        box_radius = li + a

        self.load()
        return self._new(self.im.box_blur(box_radius, n))
