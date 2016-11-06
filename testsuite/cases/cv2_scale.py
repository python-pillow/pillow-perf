# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import cv2

from .base import rpartial, BaseScaleCase
from .cv2 import Cv2TestCase


class ScaleCase(BaseScaleCase, Cv2TestCase):
    def runner(self, im):
        cv2.resize(im, self.dest_size, interpolation=self.filter)


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
