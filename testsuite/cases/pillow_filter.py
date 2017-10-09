# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial
from .pillow import ImageFilter, PillowTestCase


class FilterCase(PillowTestCase):
    def handle_args(self, filter):
        self.filter = filter

    def runner(self, im):
        im.filter(self.filter)

    def readable_args(self):
        return [self.filter.name]


cases = [
    rpartial(FilterCase, ImageFilter.SMOOTH),
    rpartial(FilterCase, ImageFilter.SHARPEN),
    rpartial(FilterCase, ImageFilter.SMOOTH_MORE),
]
