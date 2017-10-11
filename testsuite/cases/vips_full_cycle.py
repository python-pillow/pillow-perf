# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, root, FullCycleBaseCase
from .vips import Image


class FullCycleCase(FullCycleBaseCase):
    def runner(self):
        im = Image.new_from_file(root('resources', self.filename))
        if self.level > 0:
            im = im.rot90()
            if self.level > 1:
                im = im.resize(0.4, kernel="cubic")
                if self.level > 2:
                    im = im.gaussblur(4, min_ampl=0.07)

        im.write_to_buffer('.'+self.filetype, Q=85)
        # im.write_to_file('../_out.{}.vips.png'.format(self.level))


cases = [
    rpartial(FullCycleCase, 0, 'Load+save', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 1, '+transpose', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 2, '+resize', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 3, '+blur', 'pineapple.jpeg', 'JPEG'),
]
