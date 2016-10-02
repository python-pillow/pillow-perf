from .base import TestCase


ALL_CASES = {
    "resize": [
        TestCase(lambda: 2**10**6)
    ]
}


def collect_testsuites():
    return ALL_CASES.keys()


def load_cases(testsuite):
    return ALL_CASES[testsuite]
