# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial
from .pillow import PillowTestCase, Image


class LutCase(PillowTestCase):
    def generate_unit_table(self, channels, size):
        if isinstance(size, tuple):
            size1D, size2D, size3D = size
        else:
            size1D, size2D, size3D = (size, size, size)

        table = [
            [
                r / float(size1D-1),
                g / float(size2D-1),
                b / float(size3D-1),
                r / float(size1D-1),
            ][:channels]
            for b in range(size3D)
                for g in range(size2D)
                    for r in range(size1D)
        ]
        return (
            channels, size1D, size2D, size3D,
            [item for sublist in table for item in sublist])

    def handle_args(self, channels, table_size):
        self.channels = channels
        self.table_size = table_size
        self.to_mode = 'RGB' if channels == 3 else 'RGBA'
        self.table = self.generate_unit_table(channels, table_size)

    def runner(self, im):
        im._new(im.im.color_lut_3d(self.to_mode, Image.LINEAR, *self.table))

    def readable_args(self):
        return ["{}³ to {}D".format(self.table_size, self.channels)]


cases = [
    rpartial(LutCase, 3, 5),
    rpartial(LutCase, 3, 17),
    rpartial(LutCase, 3, 33),
    rpartial(LutCase, 4, 5),
    rpartial(LutCase, 4, 17),
    rpartial(LutCase, 4, 33),
]
