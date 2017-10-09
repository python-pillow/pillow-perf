# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, root, BaseLoadCase, BaseSaveCase
from .pgmagick import Image, Blob


class LoadCase(BaseLoadCase):
    def runner(self):
        Image(root('resources', self.filename).encode('utf-8'))


class SaveCase(BaseSaveCase):
    def create_test_data(self):
        im = Image(root('resources', self.filename).encode('utf-8'))
        return [im]

    def runner(self, im):
        im.quality(85)
        im.magick(self.filetype.encode('utf-8'))
        im.write(Blob())


cases = [
    rpartial(LoadCase, 'JPEG', 'pineapple.jpeg'),
    rpartial(SaveCase, 'JPEG', 'pineapple.jpeg'),
]
