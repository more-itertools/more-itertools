from __future__ import division, print_function, unicode_literals

from doctest import DocTestSuite


def load_tests(loader, tests, ignore):
    # Add the doctests
    tests.addTests(DocTestSuite('more_itertools.examples'))
    return tests
