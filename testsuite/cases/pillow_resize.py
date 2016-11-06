# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import rpartial
from .pillow import PillowTestCase


class ResizeCase(PillowTestCase):
    def handle_args(self, dest_size, filter, hpass=True, vpass=True):
        self.dest_size = dest_size
        self.filter = filter
        self.hpass = hpass
        self.vpass = vpass

    def runner(self, im):
        self.update_dest_size(im)
        return self.resize(im, self.calc_dest_size, self.filter)

    def readable_args(self):
        return [
            "x".join(map(str, self.calc_dest_size)),
            self.filter_ids.get(self.filter, self.filter),
        ]

    def update_dest_size(self, im):
        self.calc_dest_size = [
            self.dest_size[0] if self.hpass else im.size[0],
            self.dest_size[1] if self.vpass else im.size[1],
        ]


cases = [
    rpartial(ResizeCase, size, flt, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for size in [
        (16, 16),
        (320, 180),
        (1920, 1200),
        (7712, 4352),
    ] for flt in [
        # Image.NEAREST,
        # Image.BOX,
        Image.BILINEAR,
        # Image.HAMMING,
        Image.BICUBIC,
        Image.LANCZOS,
    ]
]
