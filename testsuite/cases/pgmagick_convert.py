from .base import rpartial, BaseConvertCase
from .pgmagick import Image, ImageType, PgmagickTestCase


class ConvertCase(BaseConvertCase, PgmagickTestCase):
    def runner(self, im):
        im = Image(im)
        if self.mode_to == 'L':
            im.type(ImageType.GrayscaleType)
        elif self.mode_to in 'LA':
            im.type(ImageType.GrayscaleMatteType)
        else:
            raise ValueError('Unknown mode: {}'.format(self.mode_to))


cases = [
    rpartial(ConvertCase, 'RGB', 'L'),
    rpartial(ConvertCase, 'RGBA', 'LA'),
]
