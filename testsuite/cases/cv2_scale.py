from .base import rpartial, BaseScaleCase
from .cv2 import cv2, Cv2TestCase


class ScaleCase(BaseScaleCase, Cv2TestCase):
    def runner(self, im):
        cv2.resize(im, self.dest_size, interpolation=self.filter)


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
    ] for flt in [
        # cv2.INTER_NEAREST,
        cv2.INTER_AREA,
    ]
] + [
    rpartial(ScaleCase, scale, flt, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for scale in [
        2.14,
    ] for flt in [
        # cv2.INTER_NEAREST,
        cv2.INTER_LINEAR,
        cv2.INTER_CUBIC,
        cv2.INTER_LANCZOS4,
    ]
]
