# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from importlib import import_module


def collect_test_suites():
    return [
        "load", "convert", "composition", "rotate_right",
        "scale", "blur",

        "wand_load", "wand_rotate_right", "wand_scale",

        "cv2_load", "cv2_rotate_right", "cv2_blur",
    ]


def load_cases(test_suite, args):
    try:
        # Try to load Pillow test first
        module = import_module('.pillow_' + test_suite, 'cases')
    except ImportError:
        module = import_module('.' + test_suite, 'cases')
    return module.cases
