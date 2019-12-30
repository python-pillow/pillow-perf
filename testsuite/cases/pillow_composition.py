from .base import rpartial, root
from .pillow import Image, PillowTestCase


class CompositionCase(PillowTestCase):
    def create_test_data(self):
        im = Image.open(root('resources', 'color_circle.png'))
        im = self.resize(im, self.size, Image.BICUBIC)
        return [im, im.copy()]

    def runner(self, first, second):
        Image.alpha_composite(first, second)

    def readable_args(self):
        return ["Composition"]


cases = [
    rpartial(CompositionCase),
]
