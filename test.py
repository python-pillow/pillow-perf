#!/usr/bin/env python

from PIL import Image, ImageOps
import time
import sys


Image.LANCZOS = Image.ANTIALIAS


def blur(im, *args):
    return im._new(ImageOps.gaussian_blur(im, *args))


def split(im):
    im._splitted = im.split()
    return im._splitted[0]


def merge(im):
    return Image.merge(im.mode, im._splitted)


def resize(im, size, method):
    return im._new(im.im.stretch(size, method))


im = Image.open(sys.argv[1])
im.load()

for method, args, desc in [
    (Image.Image.resize, ((16, 16), Image.BILINEAR), '16x16 bil'),
    (Image.Image.resize, ((16, 16), Image.BICUBIC),  '16x16 bic'),
    (Image.Image.resize, ((16, 16), Image.LANCZOS),  '16x16 lzs'),
    (Image.Image.resize, ((320, 180), Image.BILINEAR), '320x180 bil'),
    (Image.Image.resize, ((320, 180), Image.BICUBIC),  '320x180 bic'),
    (Image.Image.resize, ((320, 180), Image.LANCZOS),  '320x180 lzs'),
    (Image.Image.resize, ((1920, 1200), Image.BILINEAR), '1920x1200 bil'),
    (Image.Image.resize, ((1920, 1200), Image.BICUBIC),  '1920x1200 bic'),
    (Image.Image.resize, ((1920, 1200), Image.LANCZOS),  '1920x1200 lzs'),
    (Image.Image.resize, ((7712, 4352), Image.BILINEAR), '7712x4352 bil'),
    (Image.Image.resize, ((7712, 4352), Image.BICUBIC),  '7712x4352 bic'),
    (Image.Image.resize, ((7712, 4352), Image.LANCZOS),  '7712x4352 lzs'),
    (blur, (1,), 'blur 1px'),
    (blur, (10,), 'blur 10px'),
    (blur, (100,), 'blur 100px'),
]:
    times = []
    for _ in range(22):
        start = time.time()
        method(im, *args)
        times.append(time.time() - start)

        sys.stdout.write('.')
        sys.stdout.flush()

    try:
        method(im, *args).save('_pil ' + desc + '.png', compress_level=1)
    except Exception:
        method(im, *args).convert('RGBA').save('_res ' + desc + '.png', compress_level=1)
        pass

    times.sort()
    median_duration = times[len(times) // 2]
    min_duration = times[0]
    pixels = im.size[0] * im.size[1]
    print '\r>>> {:14} {:8.5f} s {:8.2f} Mpx/s {:8.2f} Mpx/s'.format(
        desc,
        median_duration, pixels / median_duration / 1000 / 1000,
        pixels / min_duration / 1000 / 1000,
    )

im = None
# time.sleep(10)
