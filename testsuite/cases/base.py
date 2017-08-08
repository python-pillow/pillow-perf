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
        self.data = self.create_test_data()

    def handle_args(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def create_test_data(self):
        return []

    def run(self):
        start = time.time()
        for _ in range(self.repeat):
            self.runner(*self.data)
        return (time.time() - start) / self.repeat

    __call__ = run

    def readable_args(self):
        return list(map(str, self.args))

    def readable_name(self):
        return " ".join(self.readable_args())


class BaseScaleCase(object):
    def handle_args(self, scale, filter, hpass=True, vpass=True):
        self.scale = scale
        self.filter = filter
        self.hpass = hpass
        self.vpass = vpass
        self.dest_size = (
            int(round(scale * self.size[0])) if hpass else self.size[0],
            int(round(scale * self.size[1])) if vpass else self.size[1],
        )

    def readable_args(self):
        return [
            "x".join(map(str, self.dest_size)),
            self.filter_ids.get(self.filter, self.filter),
        ]

    def readable_name(self):
        return 'to ' + super(BaseScaleCase, self).readable_name()


class BaseConvertCase(object):
    def handle_args(self, mode, mode_to):
        self.mode = mode
        self.mode_to = mode_to

    def readable_args(self):
        return ["{} to {}".format(self.mode, self.mode_to)]


class BaseAllocateCase(BaseTestCase):
    def handle_args(self, mode):
        self.mode = mode

    def readable_args(self):
        return ['mode ' + self.mode]


class BaseSplitCase(object):
    def handle_args(self, mode):
        self.mode = mode

    def readable_args(self):
        return ["split {}".format(self.mode)]


class BaseGetBandCase(object):
    def handle_args(self, mode, band):
        self.mode = mode
        self.band = band

    def readable_args(self):
        return ["get {} of {}".format(self.mode[self.band], self.mode)]


class BaseMergeCase(object):
    def create_test_data(self):
        data = super(BaseMergeCase, self).create_test_data()
        return [data[0].split()]

    def handle_args(self, mode):
        self.mode = mode

    def readable_args(self):
        return ["merge {}".format(self.mode)]


class BaseCropCase(object):
    def handle_args(self, scale):
        self.scale = scale
        width = int(round(scale[0] * self.size[0]))
        height = int(round(scale[1] * self.size[1]))
        top = int((self.size[0] - width) / 2)
        left = int((self.size[1] - height) / 2)
        self.dest_size = (width, height)
        self.dest_box = (top, left, width + top, height + left)

    def readable_args(self):
        return ["x".join(map(str, self.dest_size))]
