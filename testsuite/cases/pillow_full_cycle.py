# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from .base import rpartial, root, BaseTestCase
from .pillow import Image, ImageFilter


class FullCycleCase(BaseTestCase):
    def handle_args(self, filetype, filename):
        self.filetype = filetype
        self.filename = filename
        self.args = ()

    def runner(self):
        im = Image.open(root('resources', self.filename))
        im = im.transpose(Image.ROTATE_270)
        size = (int(im.width * 0.4 + 0.5), int(im.height * 0.4 + 0.5))
        im = im.resize(size, Image.BICUBIC)
        im = im.filter(ImageFilter.GaussianBlur(4))

        im.save(BytesIO(), format=self.filetype, quality=85)
        # im.save('../_out.pillow.png')


cases = [
    rpartial(FullCycleCase, 'JPEG', 'pineapple.jpeg'),
]
