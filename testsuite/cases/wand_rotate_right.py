# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from wand.image import Image

from .base import rpartial
from .wand import WandTestCase


class RotateRightCase(WandTestCase):
    def handle_args(self, name, transposition):
        self.name = name
        self.transposition = transposition

    def runner(self, im):
        with im.clone() as im:
            self.transposition(im)

    def readable_args(self):
        return [self.name]


cases = [
    rpartial(RotateRightCase, 'Flop', Image.flop),
    rpartial(RotateRightCase, 'Flip', Image.flip),
    rpartial(RotateRightCase, 'Rotate 90',
             rpartial(Image.rotate, degree=270.0)),
    rpartial(RotateRightCase, 'Rotate 180',
             rpartial(Image.rotate, degree=180.0)),
    rpartial(RotateRightCase, 'Rotate 270',
             rpartial(Image.rotate, degree=90.0)),
    rpartial(RotateRightCase, 'Transpose', Image.transpose),
]
