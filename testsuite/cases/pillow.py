# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import BaseTestCase


Image.LANCZOS = Image.ANTIALIAS

class PillowTestCase(BaseTestCase):
    filter_ids = {
        0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        4: 'box', 5: 'hmn', 6: 'mtc',
    }

    def create_test_data(self, size, mode):
        return [Image.new(mode, size)]

    @classmethod
    def resize(cls, self, size, resample=Image.NEAREST):
        self.load()

        if self.size == size:
            return self._new(self.im)

        if self.mode in ("1", "P"):
            resample = Image.NEAREST

        if self.mode == 'RGBA':
            return cls.resize(self.convert('RGBa'), size, resample).convert('RGBA')

        if self.mode == 'LA':
            return cls.resize(self.convert('La'), size, resample).convert('LA')

        if resample == Image.NEAREST:
            im = self.im.resize(size, resample)
        else:
            im = self.im.stretch(size, resample)

        return self._new(im)
