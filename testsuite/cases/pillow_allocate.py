from .base import (rpartial, BaseAllocateCase, BaseSplitCase, BasePackCase,
                   BaseGetBandCase, BaseMergeCase, BaseUnpackCase)
from .pillow import Image, PillowTestCase


class AllocateCase(BaseAllocateCase):
    def runner(self):
        Image.new(self.mode, self.size)


class UnpackCase(BaseUnpackCase, PillowTestCase):
    def create_test_data(self):
        im = super().create_test_data()[0]
        return [im, im.tobytes()]

    def runner(self, im, data):
        im.frombytes(data)


class PackCase(BasePackCase, PillowTestCase):
    def runner(self, im):
        im.tobytes()


class SplitCase(BaseSplitCase, PillowTestCase):
    def runner(self, im):
        im.split()


class GetBandCase(BaseGetBandCase, PillowTestCase):
    def runner(self, im):
        self.getchannel(im, self.band)


class MergeCase(BaseMergeCase, PillowTestCase):
    def runner(self, bands):
        Image.merge(self.mode, bands)


cases = [
    rpartial(AllocateCase, 'L'),
    rpartial(AllocateCase, 'LA'),
    rpartial(AllocateCase, 'RGB'),
    rpartial(AllocateCase, 'RGBA'),
    rpartial(UnpackCase, 'L'),
    rpartial(UnpackCase, 'LA'),
    rpartial(UnpackCase, 'RGB'),
    rpartial(UnpackCase, 'RGBA'),
    rpartial(PackCase, 'L'),
    rpartial(PackCase, 'LA'),
    rpartial(PackCase, 'RGB'),
    rpartial(PackCase, 'RGBA'),
    rpartial(SplitCase, 'LA'),
    rpartial(SplitCase, 'RGB'),
    rpartial(SplitCase, 'RGBA'),
    rpartial(GetBandCase, 'RGB', 0),
    rpartial(GetBandCase, 'RGBA', 3),
    rpartial(MergeCase, 'LA'),
    rpartial(MergeCase, 'RGB'),
    rpartial(MergeCase, 'RGBA'),
]
