# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import cv2

from .base import rpartial, root, BaseLoadCase


class LoadCase(BaseLoadCase):
    def runner(self):
        cv2.imread(root('resources', self.filename),
                   flags=cv2.IMREAD_UNCHANGED)


cases = [
    rpartial(LoadCase, 'JPEG', 'pineapple.jpeg'),
]
