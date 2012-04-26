from unittest import TestCase

from nose.tools import eq_

from more_itertools import collate, chunked


class CollateTests(TestCase):
    """Unit tests for collate()"""
    # Also accidentally tests peekable, though that could use its own tests

    def test_default(self):
        """Test with the default `key` function."""
        iterables = [xrange(4), xrange(7), xrange(3, 6)]
        eq_(sorted(reduce(list.__add__, [list(it) for it in iterables])),
            list(collate(*iterables)))

    def test_key(self):
        """Test using a custom `key` function."""
        iterables = [xrange(5, 0, -1), xrange(4, 0, -1)]
        eq_(list(sorted(reduce(list.__add__,
                                        [list(it) for it in iterables]),
                        reverse=True)),
            list(collate(*iterables, key=lambda x: -x)))

    def test_empty(self):
        """Be nice if passed an empty list of iterables."""
        eq_([], list(collate()))

    def test_one(self):
        """Work when only 1 iterable is passed."""
        eq_([0, 1], list(collate(xrange(2))))

    def test_reverse(self):
        """Test the `reverse` kwarg."""
        iterables = [xrange(4, 0, -1), xrange(7, 0, -1), xrange(3, 6, -1)]
        eq_(sorted(reduce(list.__add__, [list(it) for it in iterables]),
                   reverse=True),
            list(collate(*iterables, reverse=True)))


class ChunkedTests(TestCase):
    """Tests for chunked()"""

    def test_even(self):
        """Test when ``n`` divides evenly into the length of the iterable."""
        eq_(list(chunked('ABCDEF', 3)), [('A', 'B', 'C'), ('D', 'E', 'F')])

    def test_odd(self):
        """Test when ``n`` does not divide evenly into the length of the iterable."""
        eq_(list(chunked('ABCDE', 3)), [('A', 'B', 'C'), ('D', 'E')])
