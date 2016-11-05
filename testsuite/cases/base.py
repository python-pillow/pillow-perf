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

    def handle_args(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def create_test_data(self, size, mode):
        return []

    def run(self):
        test_data = self.create_test_data(self.size, self.mode)
        self.prepare_runner()
        start = time.time()
        for _ in range(self.repeat):
            self.runner(*test_data)
        return (time.time() - start) / self.repeat

    __call__ = run

    def prepare_runner(self):
        pass

    def readable_args(self):
        return list(map(str, self.args))
