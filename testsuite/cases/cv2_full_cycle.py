from math import ceil

from .base import rpartial, root, FullCycleBaseCase
from .cv2 import cv2


class FullCycleCase(FullCycleBaseCase):
    def runner(self):
        im = cv2.imread(root('resources', self.filename),
                        flags=cv2.IMREAD_UNCHANGED)

        if self.level > 0:
            im = cv2.flip(cv2.transpose(im), 1)

        if self.level > 1:
            size = (int(im.shape[1] * 0.4 + 0.5),
                    int(im.shape[0] * 0.4 + 0.5))
            im = cv2.resize(im, size, interpolation=cv2.INTER_AREA)

        if self.level > 2:
            window = 1 + int(ceil(4 * 2.5)) * 2
            im = cv2.GaussianBlur(im, (window, window), 4)

        cv2.imencode("." + self.filetype, im,
                     [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        # cv2.imwrite('../_out.{}.cv2.png'.format(self.level), im)


cases = [
    rpartial(FullCycleCase, 0, 'Load+save', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 1, '+transpose', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 2, '+resize', 'pineapple.jpeg', 'JPEG'),
    rpartial(FullCycleCase, 3, '+blur', 'pineapple.jpeg', 'JPEG'),
]
