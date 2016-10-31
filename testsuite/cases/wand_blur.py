# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial
from .wand import WandTestCase


class BlurCase(WandTestCase):
    def handle_args(self, radius):
        self.radius = radius

    def runner(self, im):
        with im.clone() as im:
            im.gaussian_blur(2.5 * self.radius, self.radius)

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
