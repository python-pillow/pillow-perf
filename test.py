#!/usr/bin/env python

from PIL import Image, ImageOps
import time
import sys

Image.LANCZOS = Image.ANTIALIAS


class TestCase(object):
    runner = None

    def __init__(self, *args, **kwargs):
        self.args = args
        if 'desc' in kwargs:
            self.desc = kwargs['desc']

    def prepare(self, im):
        im.load()
        return im

    def run(self, im):
        start = time.time()
        self._result = None
        self._result = self.runner(im, *self.args)
        return time.time() - start

    @property
    def result(self):
        return self._result

    def processed_pixels(self, im):
        return im.size[0] * im.size[1]

    def cleanup(self):
        self._result = None


class ResizeCase(TestCase):
    runner = staticmethod(Image.Image.resize)

    @property
    def desc(self):
        flt = {
            0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        }.get(self.args[1], self.args[1])
        return "{size[0]}x{size[1]} {flt}".format(size=self.args[0], flt=flt)


class BlurCase(TestCase):
    def runner(self, im, radius):
        return im._new(ImageOps.gaussian_blur(im, radius))

    @property
    def desc(self):
        return "blur {radius}px".format(radius=self.args[0])


class ConvertCase(TestCase):
    runner = staticmethod(Image.Image.convert)

    def prepare(self, im):
        im.load()
        mode = self.args[0]
        if mode == 'RGBA':
            im = im.convert('RGBa')
        return im

    @property
    def desc(self):
        return "convert {mode}".format(mode=self.args[0])

    @property
    def result(self):
        if self._result.mode == 'RGBa':
            self._result = self._result.convert('RGBA')
        return self._result


class RotateCase(TestCase):
    runner = staticmethod(Image.Image.rotate)

    @property
    def desc(self):
        flt = {
            0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        }.get(self.args[1], self.args[1])
        return "rotate {mode} {flt} ".format(mode=self.args[0], flt=flt) + (
            'ex' if self.args[2] else '  ')


class CreateCase(TestCase):
    times = 10

    def prepare(self, im):
        pass

    def runner(self, im, *args):
        for i in range(self.times):
            Image.new(*args)
        return im

    @property
    def desc(self):
        return "create {mode} {size}".format(
            mode=self.args[0], size=self.args[1])

    def processed_pixels(self, im):
        size = self.args[1]
        return size[0] * size[1] * self.times


test_cases = [
    # ResizeCase((16, 16), Image.NEAREST),
    # ResizeCase((16, 16), Image.BILINEAR),
    # ResizeCase((16, 16), Image.BICUBIC),
    # ResizeCase((16, 16), Image.LANCZOS),
    # ResizeCase((320, 180), Image.NEAREST),
    # ResizeCase((320, 180), Image.BILINEAR),
    # ResizeCase((320, 180), Image.BICUBIC),
    # ResizeCase((320, 180), Image.LANCZOS),
    # ResizeCase((1920, 1200), Image.NEAREST),
    # ResizeCase((1920, 1200), Image.BILINEAR),
    # ResizeCase((1920, 1200), Image.BICUBIC),
    # ResizeCase((1920, 1200), Image.LANCZOS),
    # ResizeCase((7712, 4352), Image.NEAREST),
    # ResizeCase((7712, 4352), Image.BILINEAR),
    # ResizeCase((7712, 4352), Image.BICUBIC),
    # ResizeCase((7712, 4352), Image.LANCZOS),
    # BlurCase(1),
    # BlurCase(10),
    # BlurCase(100),
    # ConvertCase('RGBa'),
    # ConvertCase('RGBA'),
    # RotateCase(10, Image.NEAREST, False),
    # RotateCase(10, Image.NEAREST, True),
    # RotateCase(10, Image.BICUBIC, False),
    # RotateCase(10, Image.BICUBIC, True),
    # RotateCase(45, Image.NEAREST, False),
    # RotateCase(45, Image.NEAREST, True),
    # RotateCase(45, Image.BICUBIC, False),
    # RotateCase(45, Image.BICUBIC, True),
    # RotateCase(89.9, Image.NEAREST, False),
    # RotateCase(89.9, Image.NEAREST, True),
    # RotateCase(89.9, Image.BICUBIC, False),
    # RotateCase(89.9, Image.BICUBIC, True),
    # RotateCase(90, Image.NEAREST, False),
    # RotateCase(90, Image.NEAREST, True),
    # RotateCase(90, Image.BICUBIC, False),
    # RotateCase(90, Image.BICUBIC, True),
    CreateCase('RGB', (256, 256)),
    CreateCase('RGB', (1280, 1280)),
    CreateCase('RGB', (2560, 2560)),
    CreateCase('RGB', (81920, 80)),
    CreateCase('RGB', (80, 81920)),
]

for case in test_cases:
    im = case.prepare(Image.open(sys.argv[1]))
    pixels = case.processed_pixels(im)

    times = []
    for _ in range(11):
        times.append(case.run(im))
        sys.stdout.write('.')
        sys.stdout.flush()
    times.sort()
    median_duration = times[len(times) // 2]
    min_duration = times[0]
    print '\r>>> {:14} {:8.5f} s {:8.2f} Mpx/s {:8.2f} Mpx/s'.format(
        case.desc,
        median_duration, pixels / median_duration / 1000 / 1000,
        pixels / min_duration / 1000 / 1000,
    )

    im = None
    if '--save' in sys.argv:
        case.result.save('_pil ' + case.desc + '.png', compress_level=1)
    case.cleanup()

# time.sleep(10)
