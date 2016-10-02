#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import time
import sys

from cases import collect_testsuites



def run_cases(testsuites, size, mode, times, stdout=False):
    for testsuite in testsuites:
        test_cases = load_cases(testsuite)

        for case in testsuite:
            runs = []

            with case.prepare(size, mode) as run:
                for _ in range(times):
                    runs.append(run())
                    sys.stdout.write('.')
                    sys.stdout.flush()

            runs.sort()
            median_duration = runs[times // 2]
            min_duration = runs[0]

            pixels = size[0] * size[1]
            yield {
                "testsuite": testsuite,
                "case": case,
                "median_duration": median_duration,
                "median_fillrate": pixels / median_duration / 1000 / 1000,
                "min_duration": min_duration,
                "min_fillrate": pixels / min_duration / 1000 / 1000,
            }


def pixel_size(arg):
    for sep in [',', 'x', '×']:
        if sep in arg:
            arg = arg.split(sep)
            if len(arg) != 2:
                raise ValueError('More than two dimensions')
            return list(map(int, arg))

    raise ValueError('No separator found')


def argument_parser(testsuites):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('testsuite', nargs='+',
                        choices=testsuites, metavar='testsuite')
    parser.add_argument('--size', '-s',type=pixel_size, default=[2560, 1600])
    parser.add_argument('--mode', '-m',
                        choices=["RGB", "RGBA", "RGBa", "L"], default="RGB")
    parser.add_argument('--runs', '-n', type=int, default=11)
    parser.add_argument('--sleep', action='store_true')
    return parser


if __name__ == '__main__':
    testsuites = collect_testsuites()
    args = argument_parser(testsuites).parse_args()

    run_cases(args.testsuite, args.size, args.mode, args.runs, stdout=True)

    if args.sleep:
        time.sleep(10)
