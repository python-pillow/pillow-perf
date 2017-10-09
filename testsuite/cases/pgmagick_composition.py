# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, root
from .pgmagick import Image, Geometry, FilterTypes, PgmagickTestCase


class CompositionCase(PgmagickTestCase):
    def create_test_data(self):
        im = Image(root('resources', 'color_circle.png').encode('utf-8'))
        im.filterType(FilterTypes.CatromFilter)
        im.scale(Geometry(b"{}x{}!".format(self.size[0], self.size[1])))
        return [im, Image(im)]

    def runner(self, first, second):
        res = Image(first)
        res.composite(second, 0, 0)

    def readable_args(self):
        return ["Composition"]


cases = [
    rpartial(CompositionCase),
]
