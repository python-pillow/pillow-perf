# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from .resize import cases as resize_cases
from .scale import cases as scale_cases
from .blur import cases as blur_cases
from .convert import cases as convert_cases
from .composition import cases as composition_cases

from .wand_resize import cases as wand_resize_cases
from .wand_scale import cases as wand_scale_cases


ALL_CASES = {
    "resize": resize_cases,
    "scale": scale_cases,
    "blur": blur_cases,
    "convert": convert_cases,
    "composition": composition_cases,

    "wand_resize": wand_resize_cases,
    "wand_scale": wand_scale_cases,
}


def collect_testsuites():
    return ALL_CASES.keys()


def load_cases(testsuite):
    return ALL_CASES[testsuite]
