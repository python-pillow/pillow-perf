# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from PIL import Image

from .base import rpartial, root, BaseTestCase


class LoadCase(BaseTestCase):
    def handle_args(self, filetype, filename):
        self.filetype = filetype
        self.filename = filename

    def runner(self):
        im = Image.open(root('resources', self.filename))
        im.load()

    def readable_args(self):
        return ["{} load".format(self.filetype)]


class SaveCase(BaseTestCase):
    def handle_args(self, filetype, filename):
        self.filetype = filetype
        self.filename = filename

    def create_test_data(self):
        im = Image.open(root('resources', self.filename))
        im.load()
        return [im]

    def runner(self, im):
        im.save(BytesIO(), format=self.filetype)

    def readable_args(self):
        return ["{} save".format(self.filetype)]


cases = [
    rpartial(LoadCase, 'Jpeg', 'pineapple.jpeg'),
    rpartial(SaveCase, 'Jpeg', 'pineapple.jpeg'),
]
