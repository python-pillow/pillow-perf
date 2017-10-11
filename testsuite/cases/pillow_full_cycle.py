# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from .base import rpartial, root, FullCycleBaseCase
from .pillow import Image, ImageFilter


class FullCycleCase(FullCycleBaseCase):
    def runner(self):
        im = Image.open(root('resources', self.filename))
        if self.level > 0:
            im = im.transpose(Image.ROTATE_270)
            if self.level > 1:
                size = (int(im.size[0] * 0.4 + 0.5),
                        int(im.size[1] * 0.4 + 0.5))
                im = im.resize(size, Image.BICUBIC)
                if self.level > 2:
                    im = im.filter(ImageFilter.GaussianBlur(4))

        im.save(BytesIO(), format=self.filetype, quality=85)
        # im.save('../_out.{}.pillow.png'.format(self.level))


cases = [
    rpartial(FullCycleCase, 0, 'Save/load', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 1, '+transpose', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 2, '+resize', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 3, '+blur', 'pineapple.jpeg', 'JPEG'),
]
