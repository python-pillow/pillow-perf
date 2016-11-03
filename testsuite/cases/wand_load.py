# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from wand.image import Image

from .base import rpartial, root, BaseTestCase


class LoadCase(BaseTestCase):
    def handle_args(self, filetype, filename):
        self.filetype = filetype
        self.filename = filename

    def runner(self):
        with Image(filename=root('resources', self.filename)) as im:
            pass

    def readable_args(self):
        return ["{} load".format(self.filetype)]


cases = [
    rpartial(LoadCase, 'Jpeg', 'pineapple.jpeg'),
]
