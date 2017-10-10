# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from io import BytesIO

from .base import rpartial, root, BaseTestCase
from .vips import Image, Interpolate


class FullCycleCase(BaseTestCase):
    def handle_args(self, filetype, filename):
        self.filetype = filetype
        self.filename = filename
        self.args = ()

    def runner(self):
        im = Image.new_from_file(root('resources', self.filename))
        im = im.rot90()
        im = im.resize(0.4, interpolate=Interpolate.new("bicubic"))
        im = im.gaussblur(4, min_ampl=0.01)

        im.write_to_buffer('.'+self.filetype, Q=85)
        # im.write_to_file('../_out.vips.png')


cases = [
    rpartial(FullCycleCase, 'JPEG', 'pineapple.jpeg'),
]
