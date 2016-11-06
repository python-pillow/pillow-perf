# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import cv2

from .base import BaseTestCase, root


class Cv2TestCase(BaseTestCase):
    def create_test_data(self, size, mode):
        im = cv2.imread(root('resources', 'color_circle.png'),
                        flags=cv2.IMREAD_UNCHANGED)
        if mode == 'RGB':
            im = im[:, :, :3]
        elif mode == 'RGBA':
            pass
        elif mode == 'L':
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        else:
            raise ValueError('Unknown mode: {}'.format(mode))

        # Fine for upscaling
        im = cv2.resize(im, tuple(size), interpolation=cv2.INTER_CUBIC)
        return [im]
