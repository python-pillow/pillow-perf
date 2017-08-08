# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .base import (rpartial, BaseAllocateCase, BaseSplitCase,
                   BaseGetBandCase, BaseMergeCase)
from .pillow import Image, PillowTestCase


class AllocateCase(BaseAllocateCase):
    def runner(self):
        Image.new(self.mode, self.size)


class SplitCase(BaseSplitCase, PillowTestCase):
    def runner(self, im):
        im.split()


class GetBandCase(BaseGetBandCase, PillowTestCase):
    def runner(self, im):
        im.split()[self.band]


class MergeCase(BaseMergeCase, PillowTestCase):
    def runner(self, bands):
        Image.merge(self.mode, bands)


cases = [
    rpartial(AllocateCase, 'L'),
    rpartial(AllocateCase, 'LA'),
    rpartial(AllocateCase, 'RGB'),
    rpartial(AllocateCase, 'RGBA'),
    rpartial(SplitCase, 'LA'),
    rpartial(SplitCase, 'RGB'),
    rpartial(SplitCase, 'RGBA'),
    rpartial(GetBandCase, 'RGB', 0),
    rpartial(GetBandCase, 'RGBA', 3),
    rpartial(MergeCase, 'LA'),
    rpartial(MergeCase, 'RGB'),
    rpartial(MergeCase, 'RGBA'),
]
