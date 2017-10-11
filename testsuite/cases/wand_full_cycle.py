# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from .base import rpartial, root, FullCycleBaseCase
from .wand import WandTestCase, Image


class FullCycleCase(FullCycleBaseCase, WandTestCase):
    def runner(self):
        with Image(filename=root('resources', self.filename)) as im:
            if self.level > 0:
                im.rotate(degree=90.0)
                if self.level > 1:
                    size = (int(im.width * 0.4 + 0.5),
                            int(im.height * 0.4 + 0.5))
                    im.resize(size[0], size[1], 'catrom')
                    if self.level > 2:
                        self.blur(im, 2.5 * 4, 4)

            im.compression_quality = 85
            im.format = self.filetype
            im.save(file=BytesIO())
            # im.save(filename='../_out.{}.wand.png'.format(self.level))


cases = [
    rpartial(FullCycleCase, 0, 'Load+save', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 1, '+transpose', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 2, '+resize', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 3, '+blur', 'pineapple.jpeg', 'JPEG'),
]
