#!/usr/bin/env python

import time
import sys
import argparse

from PIL import Image, ImageOps


Image.LANCZOS = Image.ANTIALIAS


class BaseTestCase(object):
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


class TestCase(BaseTestCase):
    def __init__(self, runner, *args, **kwargs):
        self.runner = runner
        super(TestCase, self).__init__(*args, **kwargs)


class ResizeCase(BaseTestCase):
    runner = staticmethod(Image.Image.resize)

    @property
    def desc(self):
        flt = {
            0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        }.get(self.args[1], self.args[1])
        return "{size[0]}x{size[1]} {flt}".format(size=self.args[0], flt=flt)


class BlurCase(BaseTestCase):
    def runner(self, im, radius):
        return im._new(ImageOps.gaussian_blur(im, radius))

    @property
    def desc(self):
        return "blur {radius}px".format(radius=self.args[0])


class ConvertCase(BaseTestCase):
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


class RotateCase(BaseTestCase):
    runner = staticmethod(Image.Image.rotate)

    @property
    def desc(self):
        flt = {
            0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        }.get(self.args[1], self.args[1])
        return "rotate {mode} {flt} ".format(mode=self.args[0], flt=flt) + (
            'ex' if self.args[2] else '  ')


class TransformCase(BaseTestCase):
    def runner(self, im, *args):
        return im.transform((512, 512), *args)

    @property
    def desc(self):
        flt = {
            0: 'ner', 1: 'lzs', 2: 'bil', 3: 'bic',
        }.get(self.args[2], self.args[2])
        return "transform {flt}".format(flt=flt)


class CreateCase(BaseTestCase):
    times = 10

    def prepare(self, im):
        pass

    def runner(self, im, *args):
        for i in range(self.times):
            Image.new(*args)
        return im

    @property
    def desc(self):
        return "new {mode} {size}".format(
            mode=self.args[0], size=self.args[1])

    def processed_pixels(self, im):
        size = self.args[1]
        return size[0] * size[1] * self.times


class CompositeCase(BaseTestCase):
    def runner(self, im, *args):
        return Image.alpha_composite(im, im)

    @property
    def desc(self):
        return "composite"


perspective_transform_data = [
    0.53009, -0.47993, 79,
    -0.31048, 0.50159, 59,
    -0.00094, -0.00131
]

affine_transform_data = [
    4, -2, 400,
    1, 3.5, -500,
]


test_cases = [
#     ResizeCase(size, flt)
#     for size in [
#         (16, 16),
#         (320, 180),
#         (1920, 1200),
#         (7712, 4352),
#     ] for flt in [
#         # Image.NEAREST,
#         Image.BILINEAR,
#         Image.BICUBIC,
#         Image.LANCZOS,
#     ]
# ] + [
#     RotateCase(deg, flt, expand)
#     for deg in [
#         10,
#         45,
#         89.9,
#         90,
#     ] for flt in [
#         Image.NEAREST,
#         # Image.BILINEAR,
#         Image.BICUBIC,
#         # Image.LANCZOS,
#     ] for expand in [
#         False,
#         True,
#     ]
# ] + [
    # BlurCase(1),
    # BlurCase(10),
    # BlurCase(100),
    # ConvertCase('RGBa'),
    # ConvertCase('RGBA'),
    # TransformCase(Image.PERSPECTIVE, perspective_transform_data, Image.NEAREST),
    # TransformCase(Image.PERSPECTIVE, perspective_transform_data, Image.BILINEAR),
    # TransformCase(Image.PERSPECTIVE, perspective_transform_data, Image.BICUBIC),
    # TransformCase(Image.AFFINE, affine_transform_data, Image.NEAREST),
    # TransformCase(Image.AFFINE, affine_transform_data, Image.BILINEAR),
    # TransformCase(Image.AFFINE, affine_transform_data, Image.BICUBIC),
    # TransformCase(Image.AFFINE, affine_transform_data, Image.LANCZOS),
    # CreateCase('RGB', (256, 256)),
    # CreateCase('RGB', (1280, 1280)),
    # CreateCase('RGB', (2560, 2560)),
    # CreateCase('RGB', (81920, 80)),
    # CreateCase('RGB', (80, 81920)),
    CompositeCase(),
]



def run_cases(test_cases, times, save=False):
    for case in test_cases:
        im = case.prepare(Image.open(sys.argv[1]))
        pixels = case.processed_pixels(im)

        runs = []
        for _ in range(times):
            runs.append(case.run(im))
            sys.stdout.write('.')
            sys.stdout.flush()
        runs.sort()
        median_duration = runs[times // 2]
        min_duration = runs[0]
        print '\r>>> {:20} {:8.5f} s {:8.2f} Mpx/s {:8.2f} Mpx/s'.format(
            case.desc,
            median_duration, pixels / median_duration / 1000 / 1000,
            pixels / min_duration / 1000 / 1000,
        )

        im = None
        if save:
            case.result.save('_pil ' + case.desc + '.png', compress_level=1)
        case.cleanup()


if __name__ == '__main__':
    run_cases(test_cases, 11, save='--save' in sys.argv)
    # time.sleep(10)
