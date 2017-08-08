# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import time
import os.path


def root(*chunks):
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', *chunks))


def rpartial(func, *args, **keywords):
    """
    right partial — same as functools.partial, but pass function args first
    """
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(fargs + args), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


class BaseTestCase(object):
    def __init__(self, size, mode, *args, **kwargs):
        self.size = size
        self.mode = mode
        self.repeat = kwargs.pop('repeat', 1)
        self.handle_args(*args, **kwargs)
        self.data = self.create_test_data(size, mode)

    def handle_args(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def create_test_data(self, size, mode):
        return []

    def run(self):
        self.prepare_runner()
        start = time.time()
        for _ in range(self.repeat):
            self.runner(*self.data)
        return (time.time() - start) / self.repeat

    __call__ = run

    def prepare_runner(self):
        pass

    def readable_args(self):
        return list(map(str, self.args))

    def readable_name(self):
        return " ".join(self.readable_args())


class BaseScaleCase(object):
    def create_test_data(self, size, mode):
        self.update_dest_size(size[0], size[1])
        return super(BaseScaleCase, self).create_test_data(size, mode)

    def handle_args(self, scale, filter, hpass=True, vpass=True):
        self.scale = scale
        self.filter = filter
        self.hpass = hpass
        self.vpass = vpass

    def readable_args(self):
        return [
            "x".join(map(str, self.dest_size)),
            self.filter_ids.get(self.filter, self.filter),
        ]

    def update_dest_size(self, width, height):
        self.dest_size = (
            int(round(self.scale * width)) if self.hpass else width,
            int(round(self.scale * height)) if self.vpass else height,
        )

    def readable_name(self):
        return 'to ' + super(BaseScaleCase, self).readable_name()


class BaseConvertCase(object):
    def handle_args(self, mode, mode_to):
        self.mode = mode
        self.mode_to = mode_to

    def create_test_data(self, size, mode):
        return super(BaseConvertCase, self).create_test_data(size, self.mode)

    def readable_args(self):
        return ["{} to {}".format(self.mode, self.mode_to)]


class BaseAllocateCase(BaseTestCase):
    def handle_args(self, mode):
        self.mode = mode

    def readable_args(self):
        return ['mode ' + self.mode]


class BaseSplitCase(object):
    def create_test_data(self, size, mode):
        return super(BaseSplitCase, self).create_test_data(size, self.mode)

    def handle_args(self, mode):
        self.mode = mode

    def readable_args(self):
        return ["split {}".format(self.mode)]


class BaseGetBandCase(object):
    def create_test_data(self, size, mode):
        return super(BaseGetBandCase, self).create_test_data(size, self.mode)

    def handle_args(self, mode, band):
        self.mode = mode
        self.band = band

    def readable_args(self):
        return ["get {} of {}".format(self.mode[self.band], self.mode)]


class BaseMergeCase(object):
    def create_test_data(self, size, mode):
        data = super(BaseMergeCase, self).create_test_data(size, self.mode)
        return [data[0].split()]

    def handle_args(self, mode):
        self.mode = mode

    def readable_args(self):
        return ["merge {}".format(self.mode)]


class BaseCropCase(object):
    def create_test_data(self, size, mode):
        self.update_dest_size(size[0], size[1])
        return super(BaseCropCase, self).create_test_data(size, mode)

    def handle_args(self, scale):
        self.scale = scale

    def readable_args(self):
        return ["x".join(map(str, self.dest_size))]

    def update_dest_size(self, width, height):
        self.dest_size = (
            int(round(self.scale[0] * width)),
            int(round(self.scale[1] * height)),
        )
        top = int((width - self.dest_size[0]) / 2)
        left = int((height - self.dest_size[1]) / 2)
        self.dest_box = (
            top, left,
            self.dest_size[0] + top,
            self.dest_size[1] + left,
        )
