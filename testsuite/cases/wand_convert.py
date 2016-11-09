# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, BaseConvertCase
from .wand import WandTestCase


class ConvertCase(BaseConvertCase, WandTestCase):
    def runner(self, im):
        with im.clone() as im:
            if self.mode_to == 'L':
                im.type = 'grayscale'
            elif self.mode_to in 'LA':
                im.type = 'grayscalematte'
            else:
                raise ValueError('Unknown mode: {}'.format(self.mode_to))


cases = [
    rpartial(ConvertCase, 'RGB', 'L'),
    rpartial(ConvertCase, 'RGBA', 'LA'),
]
