# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from wand.image import Image

from .base import rpartial, root, BaseLoadCase


class LoadCase(BaseLoadCase):
    def runner(self):
        with Image(filename=root('resources', self.filename)):
            pass


cases = [
    rpartial(LoadCase, 'JPEG', 'pineapple.jpeg'),
]
