# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, root, BaseLoadCase, BaseSaveCase
from .vips import Image


class LoadCase(BaseLoadCase):
    def runner(self):
        im = Image.new_from_file(root('resources', self.filename))
        im.getpoint(0, 0)


class SaveCase(BaseSaveCase):
    def create_test_data(self):
        im = Image.new_from_file(root('resources', self.filename))
        im.getpoint(0, 0)
        return [im]

    def runner(self, im):
        im.write_to_buffer('.'+self.filetype, Q=85)


cases = [
    rpartial(LoadCase, 'JPEG', 'pineapple.jpeg'),
    rpartial(SaveCase, 'JPEG', 'pineapple.jpeg'),
]
