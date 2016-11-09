# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, BaseConvertCase
from .pillow import PillowTestCase


class ConvertCase(BaseConvertCase, PillowTestCase):
    def runner(self, im):
        im.convert(self.mode_to)


cases = [
    rpartial(ConvertCase, 'RGB', 'L'),
    rpartial(ConvertCase, 'RGBA', 'LA'),
    rpartial(ConvertCase, 'RGBa', 'RGBA'),
    rpartial(ConvertCase, 'RGBA', 'RGBa'),
]
