#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import time
import sys
import json

from cases import collect_testsuites, load_cases


def run_test(case, times, stdout=False):
    runs = []

    for _ in range(times):
        runs.append(case())
        if stdout:
            sys.stdout.write('.')
            sys.stdout.flush()

    if stdout:
        sys.stdout.write('\r' + (' ' * times) + '\r')
        sys.stdout.flush()

    runs.sort()

    return runs[0], runs[times // 2], runs[times - 1]


def pixel_size(arg):
    for sep in [',', '*', 'x', '×']:
        if sep in arg:
            arg = arg.split(sep)
            if len(arg) != 2:
                raise ValueError('More than two dimensions')
            return (int(arg[0]), int(arg[1]))

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
    parser.add_argument('--progress', '-p', action='store_true')
    parser.add_argument('--json', '-j', action='store_true')
    return parser


if __name__ == '__main__':
    testsuites = collect_testsuites()
    args, unknown_args = argument_parser(testsuites).parse_known_args()
    pixels = args.size[0] * args.size[1]

    for testsuite in args.testsuite:
        test_cases = load_cases(testsuite)
        results = []

        print("\n###", testsuite)
        for case in test_cases:
            test = case(args.size, args.mode)
            stats = run_test(test, args.runs, args.progress)
            duration = stats[1]

            results.append((test.readable_args(), duration))

            name = " ".join(test.readable_args())
            print('    {:20} {:8.5f} s {:8.2f} Mpx/s'.format(
                name, duration, pixels / duration / 1000 / 1000,
            ))
            # free before create new test
            test = None

        if args.json:
            print(
                ",\n".join(
                    '["' + '", "'.join(readable_args) + '", ' + str(duration) + ']'
                    for readable_args, duration in results
                )
            )

    if args.sleep:
        time.sleep(10)
