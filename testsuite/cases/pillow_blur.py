from .base import rpartial
from .pillow import PillowTestCase


class BlurCase(PillowTestCase):
    def handle_args(self, radius):
        self.radius = radius

    def runner(self, im):
        self.gaussian_blur(im, self.radius)

    def readable_args(self):
        return ["{}px".format(self.radius)]


cases = [
    rpartial(BlurCase, radius)
    for radius in [
        1,
        10,
        30,
    ]
]
