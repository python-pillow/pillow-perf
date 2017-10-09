# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, BaseScaleCase
from .pgmagick import Image, FilterTypes, Geometry
from .pgmagick import PgmagickTestCase


class ScaleCase(BaseScaleCase, PgmagickTestCase):
    def runner(self, im):
        im = Image(im)
        im.filterType(self.filter)
        im.zoom(Geometry(self.dest_size[0], self.dest_size[1]))


cases = [
    rpartial(ScaleCase, size, flt, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for size in [
        0.01,
        0.125,
        0.8,
        2.14,
    ] for flt in [
        # FilterTypes.BoxFilter,
        FilterTypes.TriangleFilter,
        # FilterTypes.HammingFilter,
        FilterTypes.CatromFilter,
        FilterTypes.LanczosFilter,
    ]
]
