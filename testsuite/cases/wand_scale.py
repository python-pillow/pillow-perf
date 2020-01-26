from .base import rpartial, BaseScaleCase
from .wand import WandTestCase


class ScaleCase(BaseScaleCase, WandTestCase):
    def runner(self, im):
        with im.clone() as im:
            im.resize(self.dest_size[0], self.dest_size[1], self.filter)


cases = [
    rpartial(ScaleCase, size, flt, hpass=hpass, vpass=vpass)
    for hpass, vpass in [
        # (True, False),
        # (False, True),
        (True, True),
    ] for size in [
        0.01,
        0.125,
        0.8,
        2.14,
    ] for flt in [
        # 'box',
        'triangle',
        # 'hamming',
        'catrom',
        'lanczos',
    ]
]
