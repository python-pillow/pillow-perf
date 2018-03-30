# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial
from .pillow import PillowTestCase, Image, ImageFilter
import time


class LutCase(PillowTestCase):
    def handle_args(self, channels, table_size):
        self.channels = channels
        self.table_size = table_size
        if channels == 3:
            mode, callback = 'RGB', lambda r, g, b: (r, g, b)
        elif channels == 4:
            mode, callback = 'RGBA', lambda r, g, b: (r, g, b, r)
        else:
            raise ValueError("Channels should 3 or 4.")

        self.lut = ImageFilter.Color3DLUT.generate(
            table_size, callback, channels, mode)

    def runner(self, im):
        im.filter(self.lut)

    def readable_args(self):
        return ["{0}³ table to {1}D".format(self.table_size, self.channels)]


cases = [
    rpartial(LutCase, 3, 5),
    rpartial(LutCase, 3, 17),
    rpartial(LutCase, 3, 33),
    rpartial(LutCase, 4, 5),
    rpartial(LutCase, 4, 17),
    rpartial(LutCase, 4, 33),
]
