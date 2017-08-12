# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from .base import rpartial, root, BaseLoadCase, BaseSaveCase
from .wand import WandTestCase, Image


class LoadCase(BaseLoadCase):
    def runner(self):
        with Image(filename=root('resources', self.filename)):
            pass


class SaveCase(BaseSaveCase, WandTestCase):
    def create_test_data(self):
        im = Image(filename=root('resources', self.filename))
        self._free_resources.append(im)
        return [im]

    def runner(self, im):
        im.compression_quality = 85
        im.format = self.filetype
        im.save(file=BytesIO())


cases = [
    rpartial(LoadCase, 'JPEG', 'pineapple.jpeg'),
    rpartial(SaveCase, 'JPEG', 'pineapple.jpeg'),
]
