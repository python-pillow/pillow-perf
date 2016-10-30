# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial
from .wand_resize import ResizeCase


class ScaleCase(ResizeCase):
    def update_dest_size(self, im):
        self.calc_dest_size = [
            (int(round(self.dest_size * im.width))
                if self.hpass else im.width),
            (int(round(self.dest_size * im.height))
                if self.vpass else im.height),
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
        # 'box',
        'triangle',
        # 'hamming',
        'catrom',
        'lanczos',
    ]
]
