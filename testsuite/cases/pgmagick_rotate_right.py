from .base import rpartial
from .pgmagick import Image, PgmagickTestCase


class RotateRightCase(PgmagickTestCase):
    def handle_args(self, name, operation):
        self.name = name
        self.operation = operation

    def runner(self, im):
        im = Image(im)
        self.operation(im)

    def readable_args(self):
        return [self.name]


def transpose(im, op2):
    im.rotate(90.0)
    op2(im)

cases = [
    rpartial(RotateRightCase, 'Flop', Image.flop),
    rpartial(RotateRightCase, 'Flip', Image.flip),
    rpartial(RotateRightCase, 'Rotate 90',
             rpartial(Image.rotate, 270.0)),
    rpartial(RotateRightCase, 'Rotate 180',
             rpartial(Image.rotate, 180.0)),
    rpartial(RotateRightCase, 'Rotate 270',
             rpartial(Image.rotate, 90.0)),
    rpartial(RotateRightCase, 'Transpose', rpartial(transpose, Image.flop)),
    rpartial(RotateRightCase, 'Transverse', rpartial(transpose, Image.flip)),
]
