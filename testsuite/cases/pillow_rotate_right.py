# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import rpartial
from .pillow import PillowTestCase


class RotateRightCase(PillowTestCase):
    def handle_args(self, name, transposition):
        self.name = name
        self.transposition = transposition

    def runner(self, im):
        for trans in self.transposition:
            im = im.transpose(trans)

    def readable_args(self):
        return [self.name]


cases = [
    rpartial(RotateRightCase, 'Flop', [Image.FLIP_LEFT_RIGHT]),
    rpartial(RotateRightCase, 'Flip', [Image.FLIP_TOP_BOTTOM]),
    rpartial(RotateRightCase, 'Rotate 90', [Image.ROTATE_90]),
    rpartial(RotateRightCase, 'Rotate 180', [Image.ROTATE_180]),
    rpartial(RotateRightCase, 'Rotate 270', [Image.ROTATE_270]),
    rpartial(RotateRightCase, 'Transpose',
        [Image.TRANSPOSE]
        if hasattr(Image, 'TRANSPOSE')
        else [Image.ROTATE_90, Image.FLIP_LEFT_RIGHT]),
    rpartial(RotateRightCase, 'Transverse',
        [Image.TRANSVERSE]
        if hasattr(Image, 'TRANSVERSE')
        else [Image.ROTATE_270, Image.FLIP_LEFT_RIGHT]),
]
