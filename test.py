#!/usr/bin/env python

from PIL import Image, ImageOps
import time
import sys

Image.LANCZOS = Image.ANTIALIAS


class TestCase(object):
    def __init__(self, runner, *args, **kwargs):
        self.runner = staticmethod(runner)
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

    def cleanup(self):
        self._result = None


class ResizeCase(TestCase):
    runner = staticmethod(Image.Image.resize)

    def __init__(self, size, flt):
        self.args = (size, flt)

    @property
    def desc(self):
        flt = {
            1: 'bil', 2: 'bic', 3: 'lzs',
        }.get(self.args[1], self.args[1])
        return "{size[0]}x{size[1]} {flt}".format(size=self.args[0], flt=flt)


class BlurCase(TestCase):
    def __init__(self, radius):
        self.args = (radius,)

    def runner(self, im, radius):
        return im._new(ImageOps.gaussian_blur(im, radius))

    @property
    def desc(self):
        return "blur {radius}px".format(radius=self.args[0])


test_cases = [
    ResizeCase((16, 16), Image.BILINEAR),
    ResizeCase((16, 16), Image.BICUBIC),
    ResizeCase((16, 16), Image.LANCZOS),
    ResizeCase((320, 180), Image.BILINEAR),
    ResizeCase((320, 180), Image.BICUBIC),
    ResizeCase((320, 180), Image.LANCZOS),
    ResizeCase((1920, 1200), Image.BILINEAR),
    ResizeCase((1920, 1200), Image.BICUBIC),
    ResizeCase((1920, 1200), Image.LANCZOS),
    ResizeCase((7712, 4352), Image.BILINEAR),
    ResizeCase((7712, 4352), Image.BICUBIC),
    ResizeCase((7712, 4352), Image.LANCZOS),
    # BlurCase(1),
    # BlurCase(10),
    # BlurCase(100),
]


def split(im):
    im._splitted = im.split()
    return im._splitted[0]


def merge(im):
    return Image.merge(im.mode, im._splitted)


for case in test_cases:
    im = case.prepare(Image.open(sys.argv[1]))

    times = []
    for _ in range(11):
        times.append(case.run(im))
        sys.stdout.write('.')
        sys.stdout.flush()
    times.sort()
    median_duration = times[len(times) // 2]
    min_duration = times[0]
    pixels = im.size[0] * im.size[1]
    print '\r>>> {:14} {:8.5f} s {:8.2f} Mpx/s {:8.2f} Mpx/s'.format(
        case.desc,
        median_duration, pixels / median_duration / 1000 / 1000,
        pixels / min_duration / 1000 / 1000,
    )

    im = None
    case.result.save('_pil ' + case.desc + '.png', compress_level=1)
    case.cleanup()

# time.sleep(10)
