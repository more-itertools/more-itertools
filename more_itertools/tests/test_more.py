from itertools import islice, ifilter
from unittest import TestCase

from nose.tools import eq_, assert_raises

from more_itertools import *  # Test all the symbols are in __all__.


class CollateTests(TestCase):
    """Unit tests for ``collate()``"""
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
    """Tests for ``chunked()``"""

    def test_even(self):
        """Test when ``n`` divides evenly into the length of the iterable."""
        eq_(list(chunked('ABCDEF', 3)), [['A', 'B', 'C'], ['D', 'E', 'F']])

    def test_odd(self):
        """Test when ``n`` does not divide evenly into the length of the
        iterable.

        """
        eq_(list(chunked('ABCDE', 3)), [['A', 'B', 'C'], ['D', 'E']])


class FirstTests(TestCase):
    """Tests for ``first()``"""

    def test_many(self):
        """Test that it works on many-item iterables."""
        # Also try it on a generator expression to make sure it works on
        # whatever those return, across Python versions.
        eq_(first(x for x in xrange(4)), 0)

    def test_one(self):
        """Test that it doesn't raise StopIteration prematurely."""
        eq_(first([3]), 3)

    def test_empty_stop_iteration(self):
        """It should raise StopIteration for empty iterables."""
        assert_raises(ValueError, first, [])

    def test_default(self):
        """It should return the provided default arg for empty iterables."""
        eq_(first([], 'boo'), 'boo')


class PeekableTests(TestCase):
    """Tests for ``peekable()`` behavor not incidentally covered by testing
    ``collate()``

    """
    def test_peek_default(self):
        """Make sure passing a default into ``peek()`` works."""
        p = peekable([])
        eq_(p.peek(7), 7)

    def test_truthiness(self):
        """Make sure a ``peekable`` tests true iff there are items remaining in
        the iterable.

        """
        p = peekable([])
        self.failIf(p)
        p = peekable(xrange(3))
        self.failUnless(p)

    def test_simple_peeking(self):
        """Make sure ``next`` and ``peek`` advance and don't advance the
        iterator, respectively.

        """
        p = peekable(xrange(10))
        eq_(p.next(), 0)
        eq_(p.peek(), 1)
        eq_(p.next(), 1)


class ConsumerTests(TestCase):
    """Tests for ``consumer()``"""

    def test_consumer(self):
        @consumer
        def eater():
            while True:
                x = yield

        e = eater()
        e.send('hi')  # without @consumer, would raise TypeError


def test_ilen():
    """Sanity-check ``ilen()``."""
    eq_(ilen(ifilter(lambda x: x % 10 == 0, range(101))), 11)

class TestAppendPrepend(TestCase):
    """Tests for ``append()`` and ``prepend()``"""
    def test_append(self):
        eq_(list(append(range(5), 5)), list(range(6)))
    def test_prepend(self):
        eq_(list(prepend(range(5), -1)), list(range(-1, 5)))

class TestInterleave(TestCase):
    """Tests for ``interleave()`` and ``interleave_longest()``"""
    def test_interleave(self):
        l = [[1, 2, 3], [4, 5], [6, 7, 8]]
        eq_(list(interleave(*l)), [1, 4, 6, 2, 5, 7])
        l = [[1, 2], [3, 4, 5], [6, 7, 8]]
        eq_(list(interleave(*l)), [1, 3, 6, 2, 4, 7])
        l = [[1, 2, 3], [4, 5, 6], [7, 8]]
        eq_(list(interleave(*l)), [1, 4, 7, 2, 5, 8])
    def test_interleave_longest(self):
        l = [[1, 2, 3], [4, 5], [6, 7, 8]]
        eq_(list(interleave_longest(*l)), [1, 4, 6, 2, 5, 7, 3, 8])
        l = [[1, 2], [3, 4, 5], [6, 7, 8]]
        eq_(list(interleave_longest(*l)), [1, 3, 6, 2, 4, 7, 5, 8])
        l = [[1, 2, 3], [4, 5, 6], [7, 8]]
        eq_(list(interleave_longest(*l)), [1, 4, 7, 2, 5, 8, 3, 6])

class TestCollapse(TestCase):
    def test_collapse(self):
        l = [[1], 2, [[3], 4], [[[5]]]]
        eq_(list(collapse(l)), [1, 2, 3, 4, 5])
    def test_collapse_to_string(self):
        l = [["s1"], "s2", [["s3"], "s4"], [[["s5"]]]] 
        eq_(list(collapse(l)), ["s1", "s2", "s3", "s4", "s5"])
    def test_collapse_flatten(self):
        l = [[1], [2], [[3], 4], [[[5]]]]
        eq_(list(collapse(l, levels=1)), list(flatten(l)))
    def test_collapse_to_level(self):
        l = [[1], 2, [[3], 4], [[[5]]]]
        eq_(list(collapse(l, levels=2)), [1, 2, 3, 4, [5]])
        eq_(list(collapse(collapse(l, levels=1), levels=1)),
            list(collapse(l, levels=2)))
    def test_collapse_to_list(self):
        l = (1, [2], (3, [4, (5,)]))
        eq_(list(collapse(l, basetype=list)), [1, [2], 3, [4, (5,)]])
