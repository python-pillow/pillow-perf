# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import rpartial, BaseAllocateCase
from .pillow import  Image


class AllocateCase(BaseAllocateCase):
    def runner(self):
        Image.new(self.mode, self.size)


cases = [
    rpartial(AllocateCase, 'L'),
    rpartial(AllocateCase, 'LA'),
    rpartial(AllocateCase, 'RGB'),
    rpartial(AllocateCase, 'RGBA'),
]
