# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial
from .wand import WandTestCase


class ScaleCase(WandTestCase):
    def handle_args(self, dest_size, filter, hpass=True, vpass=True):
        self.dest_size = dest_size
        self.filter = filter
        self.hpass = hpass
        self.vpass = vpass

    def runner(self, im):
        self.update_dest_size(im)
        with im.clone() as im:
            im.resize(
                self.calc_dest_size[0],
                self.calc_dest_size[1],
                self.filter,
            )

    def readable_args(self):
        return [
            "x".join(map(str, self.calc_dest_size)),
            self.filter_ids.get(self.filter, self.filter),
        ]

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
