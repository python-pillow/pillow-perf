from .base import rpartial
from .pillow import Image, PillowTestCase


class RotateRightCase(PillowTestCase):
    def handle_args(self, name, runner):
        self.name = name
        self.runner = runner

    def readable_args(self):
        return [self.name]


cases = [
    rpartial(RotateRightCase, 'Flop',
        lambda im: im.transpose(Image.FLIP_LEFT_RIGHT)),
    rpartial(RotateRightCase, 'Flip',
        lambda im: im.transpose(Image.FLIP_TOP_BOTTOM)),
    rpartial(RotateRightCase, 'Rotate 90',
        lambda im: im.transpose(Image.ROTATE_90)),
    rpartial(RotateRightCase, 'Rotate 180',
        lambda im: im.transpose(Image.ROTATE_180)),
    rpartial(RotateRightCase, 'Rotate 270',
        lambda im: im.transpose(Image.ROTATE_270)),
    rpartial(RotateRightCase, 'Transpose',
        (lambda im: im.transpose(Image.TRANSPOSE))
        if hasattr(Image, 'TRANSPOSE')
        else lambda im: im.transpose(Image.ROTATE_90).transpose(Image.FLIP_TOP_BOTTOM)),
    rpartial(RotateRightCase, 'Transverse',
        (lambda im: im.transpose(Image.TRANSVERSE))
        if hasattr(Image, 'TRANSVERSE')
        else lambda im: im.transpose(Image.ROTATE_270).transpose(Image.FLIP_TOP_BOTTOM)),
]
