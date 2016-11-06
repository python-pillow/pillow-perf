# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from importlib import import_module


def collect_testsuites():
    return [
        "load", "convert", "composition", "rotate_right",
        "resize", "scale", "blur",

        "wand_load", "wand_rotate_right",
        "wand_resize", "wand_scale",

        "cv2_load", "cv2_rotate_right", "cv2_blur",
    ]


def load_cases(testsuite, args):
    try:
        # Try to load Pillow test first
        module = import_module('.pillow_' + testsuite, 'cases')
    except ImportError:
        module = import_module('.' + testsuite, 'cases')
    return module.cases
