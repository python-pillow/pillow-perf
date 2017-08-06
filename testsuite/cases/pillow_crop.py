# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, BaseCropCase
from .pillow import PillowTestCase


class CropCase(BaseCropCase, PillowTestCase):
    def runner(self, im):
        im = im.crop(self.dest_box)
        assert im.size == self.dest_size


cases = [
    rpartial(CropCase, (0.9, 0.9)),
    rpartial(CropCase, (1.1, 1.1)),
]
