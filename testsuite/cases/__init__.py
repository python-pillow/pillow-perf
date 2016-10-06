# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .resize import cases as resize_cases
from .scale import cases as scale_cases
from .blur import cases as blur_cases


ALL_CASES = {
    "resize": resize_cases,
    "scale": scale_cases,
    "blur": blur_cases,
}


def collect_testsuites():
    return ALL_CASES.keys()


def load_cases(testsuite):
    return ALL_CASES[testsuite]
