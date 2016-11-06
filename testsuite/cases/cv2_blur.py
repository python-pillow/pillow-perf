# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from math import ceil

import cv2

from .base import rpartial
from .cv2 import Cv2TestCase


class BlurCase(Cv2TestCase):
    def handle_args(self, radius):
        self.radius = radius

    def runner(self, im):
        window = int(ceil(self.radius * 2.5)) * 2 + 1
        cv2.GaussianBlur(im, (window, window), self.radius)

    def readable_args(self):
        return ["{}px".format(self.radius)]


cases = [
    rpartial(BlurCase, radius)
    for radius in [
        1,
        10,
        30,
    ]
]
