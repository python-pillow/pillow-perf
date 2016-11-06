# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import cv2

from .base import rpartial, root, BaseTestCase


class LoadCase(BaseTestCase):
    def handle_args(self, filetype, filename):
        self.filetype = filetype
        self.filename = filename

    def runner(self):
        cv2.imread(root('resources', self.filename))

    def readable_args(self):
        return ["{} load".format(self.filetype)]


cases = [
    rpartial(LoadCase, 'Jpeg', 'pineapple.jpeg'),
]
