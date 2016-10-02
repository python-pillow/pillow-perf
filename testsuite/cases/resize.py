# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import BaseTestCase


class ResizeCase(BaseTestCase):
    def __init__(self, size, filter, **kwargs):
        super(ResizeCase, self).__init__(size, filter, **kwargs)

        im = Image.new('RGB', (1, 1)).im
        if hasattr(im, 'stretch'):
            self.resize = Image.Image.resize

    def create_test_data(self, size, mode):
        return [Image.new(mode, size)]

    def runner(self, size, filter, im):
        if not self.kwargs.get('hpass', True):
            size = [im.size[0], size[1]]
        if not self.kwargs.get('vpass', True):
            size = [size[0], im.size[1]]
        return self.resize(im, size, filter)

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

    @property
    def desc(self):
        flt = _filters.get(self.args[1], self.args[1])
        add = ''
        if self.kwargs.get('hpass', True):
            add += 'h'
        if self.kwargs.get('vpass', True):
            add += 'v'
        return "{size[0]}x{size[1]}{add} {flt}".format(
            size=self.args[0], add=add, flt=flt)


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
