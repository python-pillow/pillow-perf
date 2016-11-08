# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import rpartial, root
from .wand import WandTestCase


class ConvertCase(WandTestCase):
    def handle_args(self, mode_from, mode_to):
        self.mode_from = mode_from
        self.mode_to = mode_to

    def create_test_data(self, size, mode):
        return super(ConvertCase, self).create_test_data(size, self.mode_from)

    def runner(self, im):
        with im.clone() as im:
            if self.mode_to == 'L':
                im.type = 'grayscale'
            elif self.mode_to in 'LA':
                im.type = 'grayscalematte'
            else:
                raise ValueError('Unknown mode: {}'.format(self.mode_to))

    def readable_args(self):
        return ["from {} to {}".format(self.mode_from, self.mode_to)]


cases = [
    rpartial(ConvertCase, 'RGBA', 'LA'),
    rpartial(ConvertCase, 'RGB', 'L'),
]
