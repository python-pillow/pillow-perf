# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import cv2

from .base import rpartial
from .cv2 import Cv2TestCase


class RotateRightCase(Cv2TestCase):
    def handle_args(self, name, runner):
        self.name = name
        self.runner = runner

    def readable_args(self):
        return [self.name]


cases = [
    rpartial(RotateRightCase, 'Flop', rpartial(cv2.flip, 1)),
    rpartial(RotateRightCase, 'Flip', rpartial(cv2.flip, 0)),
    rpartial(RotateRightCase, 'Rotate 90',
             lambda im: cv2.flip(cv2.transpose(im), 0)),
    rpartial(RotateRightCase, 'Rotate 180', rpartial(cv2.flip, -1)),
    rpartial(RotateRightCase, 'Rotate 270',
             lambda im: cv2.flip(cv2.transpose(im), 1)),
    rpartial(RotateRightCase, 'Transpose', cv2.transpose),
    rpartial(RotateRightCase, 'Transverse',
             lambda im: cv2.flip(cv2.transpose(im), -1)),
]
