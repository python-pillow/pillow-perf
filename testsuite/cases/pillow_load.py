# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from PIL import Image

from .base import rpartial, root, BaseLoadCase, BaseSaveCase


class LoadCase(BaseLoadCase):
    def runner(self):
        im = Image.open(root('resources', self.filename))
        im.load()


class SaveCase(BaseSaveCase):
    def create_test_data(self):
        im = Image.open(root('resources', self.filename))
        im.load()
        return [im]

    def runner(self, im):
        im.save(BytesIO(), format=self.filetype)


cases = [
    rpartial(LoadCase, 'JPEG', 'pineapple.jpeg'),
    rpartial(SaveCase, 'JPEG', 'pineapple.jpeg'),
]
