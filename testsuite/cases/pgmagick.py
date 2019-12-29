import os

# Make GraphicsMagick single threaded like other libraries are.
os.environ['OMP_NUM_THREADS'] = '1'


from pgmagick import Image, FilterTypes, ImageType, Geometry, Blob

from .base import BaseTestCase, root


class PgmagickTestCase(BaseTestCase):
    filter_ids = {
        FilterTypes.LanczosFilter: 'lzs',
        FilterTypes.TriangleFilter: 'bil',
        FilterTypes.CatromFilter: 'bic',
        FilterTypes.HammingFilter: 'hmn',
        FilterTypes.BoxFilter: 'box',
    }

    def create_test_data(self):
        im = Image(root('resources', 'color_circle.png').encode('utf-8'))
        if self.mode == 'RGB':
            im.type(ImageType.TrueColorType)
        elif self.mode == 'RGBA':
            im.type(ImageType.TrueColorMatteType)
        elif self.mode == 'L':
            im.type(ImageType.GrayscaleType)
        elif self.mode in 'LA':
            im.type(ImageType.GrayscaleMatteType)
        else:
            raise ValueError('Unknown mode: {}'.format(self.mode))
        im.filterType(FilterTypes.CatromFilter)
        im.zoom(Geometry(b"{}x{}!".format(self.size[0], self.size[1])))
        return [im]
