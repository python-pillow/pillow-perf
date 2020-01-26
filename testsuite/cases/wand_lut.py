from .base import rpartial, root
from .wand import WandTestCase, Image


class LutCase(WandTestCase):
    def handle_args(self, table_size, hald_image):
        self.table_size = table_size
        self.hald_image = Image(filename=hald_image)
        self._free_resources.append(self.hald_image)

    def runner(self, im):
        with im.clone() as im:
            self.hald_lut(im, self.hald_image)

    def readable_args(self):
        return ["{}³ table to 3D".format(self.table_size)]


cases = [
    rpartial(LutCase, 4, root("resources", "hald.2.png")),
    rpartial(LutCase, 16, root("resources", "hald.4.png")),
    rpartial(LutCase, 36, root("resources", "hald.6.png")),
]
