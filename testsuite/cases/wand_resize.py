# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from wand.image import Image

from .base import BaseTestCase, rpartial, root


class ResizeCase(BaseTestCase):
    filter_ids = {
        'lanczos': 'lzs', 'triangle': 'bil', 'catrom': 'bic', 'hamming': 'hmn',
    }

    def create_test_data(self, size, mode):
        im = Image(filename=root('resources', 'color_circle.png'))
        if mode == 'RGB':
            im.type = 'truecolor'
        elif mode == 'L':
            im.type = 'grayscale'
        elif mode in ('LA', 'La'):
            im.type = 'grayscalematte'
        im.resize(size[0], size[1], 'catrom')
        return [im]

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
            self.dest_size[0] if self.hpass else im.width,
            self.dest_size[1] if self.vpass else im.height,
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
        # 'box',
        'triangle',
        # 'hamming',
        'catrom',
        'lanczos',
    ]
]
