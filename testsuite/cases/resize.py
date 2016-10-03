# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import BaseTestCase


Image.LANCZOS = Image.ANTIALIAS

class ResizeCase(BaseTestCase):
    filter_ids = {
        0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        4: 'box', 5: 'hmn', 6: 'mtc',
    }

    def create_test_data(self, size, mode):
        return [Image.new(mode, size)]

    def runner(self, size, filter, im):
        size = list(size)
        if not self.kwargs.get('hpass', True):
            size[0] = im.size[0]
        if not self.kwargs.get('vpass', True):
            size[1] = im.size[1]
        return self.resize(im, size, filter)

    def readable_args(self):
        size = list(self.args[0])
        if not self.kwargs.get('hpass', True):
            size[0] = ""
        if not self.kwargs.get('vpass', True):
            size[1] = ""
        return [
            "x".join(map(str, size)),
            self.filter_ids.get(self.args[1]),
        ]

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


cases = [
    ResizeCase(size, flt, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for size in [
        (16, 16),
        (320, 180),
        (1920, 1200),
        (7712, 4352),
    ] for flt in [
        # Image.NEAREST,
        # Image.BOX,
        Image.BILINEAR,
        # Image.HAMMING,
        Image.BICUBIC,
        Image.LANCZOS,
    ]
]
