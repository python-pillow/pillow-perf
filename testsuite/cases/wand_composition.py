# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from wand.image import Image

from .base import rpartial, root
from .wand import WandTestCase


class CompositionCase(WandTestCase):
    def create_test_data(self):
        im = Image(filename=root('resources', 'color_circle.png'))
        im.resize(self.size[0], self.size[1], 'catrom')
        copy = im.clone()
        self._free_resources.append(im)
        self._free_resources.append(copy)
        return [im, copy]

    def runner(self, first, second):
        with first.clone() as res:
            res.composite(second, 0, 0)

    def readable_args(self):
        return ["Composition"]


cases = [
    rpartial(CompositionCase),
]
