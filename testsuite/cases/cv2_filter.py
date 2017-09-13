# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import numpy

from .base import rpartial
from .cv2 import Cv2TestCase, cv2


class FilterCase(Cv2TestCase):
    def handle_args(self, name, kernel):
        self.name = name
        size = int(len(kernel) ** 0.5)
        kernel = numpy.asarray(kernel, numpy.float32).reshape((size, size))
        self.kernel = kernel / kernel.sum()

    def runner(self, im):
        cv2.filter2D(im, -1, self.kernel)

    def readable_args(self):
        return [self.name]


cases = [
    rpartial(FilterCase, "Smooth", [1, 1, 1, 1, 5, 1, 1, 1, 1]),
    rpartial(FilterCase, "Sharpen", [-2, -2, -2, -2, 32, -2, -2, -2, -2]),
    rpartial(FilterCase, "Smooth More", [
        1, 1, 1, 1, 1,
        1, 5, 5, 5, 1,
        1, 5, 44, 5, 1,
        1, 5, 5, 5, 1,
        1, 1, 1, 1, 1
    ]),
]
