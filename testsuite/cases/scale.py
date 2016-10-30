# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import rpartial
from .resize import ResizeCase


class ScaleCase(ResizeCase):
    def update_dest_size(self, im):
        self.calc_dest_size = [
            (int(round(self.dest_size * im.size[0]))
                if self.hpass else im.size[0]),
            (int(round(self.dest_size * im.size[1]))
                if self.vpass else im.size[1]),
        ]


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
        # Image.NEAREST,
        # Image.BOX,
        Image.BILINEAR,
        # Image.HAMMING,
        Image.BICUBIC,
        Image.LANCZOS,
    ]
]
