from .base import rpartial, BaseScaleCase
from .pillow import Image, PillowTestCase


class ScaleCase(BaseScaleCase, PillowTestCase):
    def runner(self, im):
        self.resize(im, self.dest_size, self.filter)


cases = [
    rpartial(ScaleCase, scale, flt, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for scale in [
        0.01,
        0.125,
        0.8,
        2.14,
    ] for flt in [
        # Image.NEAREST,
        # Image.BOX,
        Image.BILINEAR,
        # Image.HAMMING,
        Image.BICUBIC,
        Image.LANCZOS,
    ]
]
