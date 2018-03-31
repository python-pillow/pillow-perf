# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, root
from .pgmagick import Image, FilterTypes, Geometry, PgmagickTestCase


class LutCase(PgmagickTestCase):
    def handle_args(self, table_size, hald_image):
        self.table_size = table_size
        self.hald_image = Image(hald_image.encode('utf-8'))

    def runner(self, im):
        im = Image(im)
        im.haldClut(self.hald_image)

    def readable_args(self):
        return ["{0}³ table to 3D".format(self.table_size)]


cases = [
    rpartial(LutCase, 4, root("resources", "hald.2.png")),
    rpartial(LutCase, 16, root("resources", "hald.4.png")),
    rpartial(LutCase, 36, root("resources", "hald.6.8.png")),
]
