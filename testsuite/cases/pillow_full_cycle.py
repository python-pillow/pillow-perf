# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from .base import rpartial, root, FullCycleBaseCase
from .pillow import Image, ImageFilter, PillowTestCase


class FullCycleCase(FullCycleBaseCase, PillowTestCase):
    def handle_args(self, *args, **kwargs):
        super(FullCycleCase, self).handle_args(*args, **kwargs)
        im = Image.open(root('resources', self.filename))
        assert im.size == self.size

    def runner(self):
        im = Image.open(root('resources', self.filename))

        if self.level > 0:
            size = (int(im.size[0] * 0.5 + 0.5),
                    int(im.size[1] * 0.5 + 0.5))
            im = self.resize(im, size, Image.LANCZOS)

        if self.level > 1:
            im = im.filter(ImageFilter.SHARPEN)

        im.save(BytesIO(), format=self.filetype, quality=85)
        # im.save('../_out.{}.pillow.jpeg'.format(self.level))


cases = [
    rpartial(FullCycleCase, 0, 'Load+save', 'pineapple.1920.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 1, '+resize', 'pineapple.1920.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 2, '+sharp', 'pineapple.1920.jpeg', 'JPEG'),
]
