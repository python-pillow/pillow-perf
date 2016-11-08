# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import rpartial, root
from .pillow import PillowTestCase


class ConvertCase(PillowTestCase):
    def handle_args(self, mode_from, mode_to):
        self.mode_from = mode_from
        self.mode_to = mode_to

    def create_test_data(self, size, mode):
        return super(ConvertCase, self).create_test_data(size, self.mode_from)

    def runner(self, im):
        im.convert(self.mode_to)

    def readable_args(self):
        return ["from {} to {}".format(self.mode_from, self.mode_to)]


cases = [
    rpartial(ConvertCase, 'RGBa', 'RGBA'),
    rpartial(ConvertCase, 'RGBA', 'RGBa'),
    rpartial(ConvertCase, 'RGBA', 'LA'),
    rpartial(ConvertCase, 'RGB', 'L'),
]
