# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import time

class BaseTestCase(object):
    runner = None

    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.kwargs = kwargs
        self.repeat = kwargs.get('repeat', 1)

    def prepare(self, size, mode):
        data = self.create_test_data(size, mode)
        return BaseRunner(self, data)

    def create_test_data(self, size, mode):
        raise NotImplementedError()

    def readable_args(self):
        return list(map(str, self.args))


class TestCase(BaseTestCase):
    def __init__(self, runner, *args, **kwargs):
        self.runner = runner
        super(TestCase, self).__init__(*args, **kwargs)

    def create_test_data(self, size, mode):
        return []


class BaseRunner():
    def __init__(self, test_case, data):
        self.test_case = test_case
        self.data = list(data)

    def cleanup(self):
        self.data = None

    def run(self):
        assert self.data is not None

        args = self.test_case.args + self.data
        start = time.time()
        for _ in range(self.test_case.repeat):
            self.test_case.runner(*args)
        return (time.time() - start) / self.test_case.repeat

    __call__ = run

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.cleanup()
