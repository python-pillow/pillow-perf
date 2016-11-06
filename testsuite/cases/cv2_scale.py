# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import cv2

from .base import rpartial
from .cv2 import Cv2TestCase


class ScaleCase(Cv2TestCase):
    def handle_args(self, scale, filter, hpass=True, vpass=True):
        self.scale = scale
        self.filter = filter
        self.hpass = hpass
        self.vpass = vpass

    def runner(self, im):
        self.update_dest_size(im.shape[1], im.shape[0])
        im = cv2.resize(im, tuple(self.dest_size),
                        interpolation=self.filter)

    def readable_args(self):
        return [
            "x".join(map(str, self.dest_size)),
            self.filter_ids.get(self.filter, self.filter),
        ]

    def update_dest_size(self, width, height):
        self.dest_size = [
            int(round(self.scale * width)) if self.hpass else width,
            int(round(self.scale * height)) if self.vpass else height,
        ]


cases = [
    rpartial(ScaleCase, scale, cv2.INTER_AREA, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for scale in [
        0.01,
        0.125,
        0.8,
    ]
] + [
    rpartial(ScaleCase, 2.14, flt, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for flt in [
        # cv2.INTER_NEAREST,
        cv2.INTER_LINEAR,
        cv2.INTER_CUBIC,
        cv2.INTER_LANCZOS4,
    ]
]
