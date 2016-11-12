from __future__ import unicode_literals

from contextlib import closing
from functools import reduce
from io import StringIO
from itertools import count, permutations
from unittest import TestCase

from nose.tools import eq_, assert_raises
from six.moves import filter, range

from more_itertools import *  # Test all the symbols are in __all__.


class CollateTests(TestCase):
    """Unit tests for ``collate()``"""
    # Also accidentally tests peekable, though that could use its own tests

    def test_default(self):
        """Test with the default `key` function."""
        iterables = [range(4), range(7), range(3, 6)]
        eq_(sorted(reduce(list.__add__, [list(it) for it in iterables])),
            list(collate(*iterables)))

    def test_key(self):
        """Test using a custom `key` function."""
        iterables = [range(5, 0, -1), range(4, 0, -1)]
        eq_(list(sorted(reduce(list.__add__,
                                        [list(it) for it in iterables]),
                        reverse=True)),
            list(collate(*iterables, key=lambda x: -x)))

    def test_empty(self):
        """Be nice if passed an empty list of iterables."""
        eq_([], list(collate()))

    def test_one(self):
        """Work when only 1 iterable is passed."""
        eq_([0, 1], list(collate(range(2))))

    def test_reverse(self):
        """Test the `reverse` kwarg."""
        iterables = [range(4, 0, -1), range(7, 0, -1), range(3, 6, -1)]
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


class IChunkedTests(TestCase):
    """Tests for ``ichunked()``"""

    def test_even(self):
        """Test when ``n`` divides evenly into the length of the iterable."""
        eq_(list(map(list, ichunked('ABCDEF', 3))), [['A', 'B', 'C'], ['D', 'E', 'F'], []])

    def test_odd(self):
        """Test when ``n`` does not divide evenly into the length of the
        iterable.

        """
        eq_(list(map(list, ichunked('ABCDE', 3))), [['A', 'B', 'C'], ['D', 'E']])

class FirstTests(TestCase):
    """Tests for ``first()``"""

    def test_many(self):
        """Test that it works on many-item iterables."""
        # Also try it on a generator expression to make sure it works on
        # whatever those return, across Python versions.
        eq_(first(x for x in range(4)), 0)

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
        self.assertFalse(p)
        p = peekable(range(3))
        self.assertTrue(p)

    def test_simple_peeking(self):
        """Make sure ``next`` and ``peek`` advance and don't advance the
        iterator, respectively.

        """
        p = peekable(range(10))
        eq_(next(p), 0)
        eq_(p.peek(), 1)
        eq_(next(p), 1)

    def test_indexing(self):
        """
        Indexing into the peekable shouldn't advance the iterator.
        """
        p = peekable('abcdefghijkl')

        # The 0th index is what ``next()`` will return
        eq_(p[0], 'a')
        eq_(next(p), 'a')

        # Indexing further into the peekable shouldn't advance the itertor
        eq_(p[2], 'd')
        eq_(next(p), 'b')

        # The 0th index moves up with the iterator; the last index follows
        eq_(p[0], 'c')
        eq_(p[9], 'l')

        eq_(next(p), 'c')
        eq_(p[8], 'l')

        # Negative indexing should fail
        with self.assertRaises(ValueError):
            p[-2]

    def test_slicing(self):
        """
        Slicing the peekable shouldn't advance the iterator.
        """
        seq = list('abcdefghijkl')
        p = peekable(seq)

        # Slicing the peekable should just be like slicing a re-iterable
        eq_(p[1:4], seq[1:4])

        # Advancing the iterator moves the slices up also
        eq_(next(p), 'a')
        eq_(p[1:4], seq[1:][1:4])

        # Implicit starts and stop should work
        eq_(p[:5], seq[1:][:5])
        eq_(p[:], seq[1:][:])

        # Indexing past the end should work
        eq_(p[:100], seq[1:][:100])

        # Steps should work, including negative
        eq_(p[::2], seq[1:][::2])
        eq_(p[::-1], seq[1:][::-1])

        # Negative indexing should fail
        with self.assertRaises(ValueError):
            p[-1:]

        with self.assertRaises(ValueError):
            p[:-1]


class ConsumerTests(TestCase):
    """Tests for ``consumer()``"""

    def test_consumer(self):
        @consumer
        def eater():
            while True:
                x = yield

        e = eater()
        e.send('hi')  # without @consumer, would raise TypeError


def test_distinct_permutations():
    """Make sure the output for ``distinct_permutations()`` is the same as
    set(permutations(it)).

    """
    iterable = ['z', 'a', 'a', 'q', 'q', 'q', 'y']
    test_output = sorted(distinct_permutations(iterable))
    ref_output = sorted(set(permutations(iterable)))
    eq_(test_output, ref_output)


def test_ilen():
    """Sanity-check ``ilen()``."""
    eq_(ilen(filter(lambda x: x % 10 == 0, range(101))), 11)


def test_with_iter():
    """Make sure ``with_iter`` iterates over and closes things correctly."""
    s = StringIO('One fish\nTwo fish')
    initial_words = [line.split()[0] for line in with_iter(closing(s))]
    eq_(initial_words, ['One', 'Two'])

    # Make sure closing happened:
    try:
        list(s)
    except ValueError:  # "I/O operation on closed file"
        pass
    else:
        raise AssertionError('StringIO object was not closed.')


def test_one():
    """Test the ``one()`` cases that aren't covered by its doctests."""
    # Infinite iterables
    numbers = count()
    assert_raises(ValueError, one, numbers)  # burn 0 and 1
    eq_(next(numbers), 2)


class IntersperseTest(TestCase):
    """ Tests for intersperse() """

    def test_intersperse(self):
        itp = intersperse('_', 'aeiou')
        assert next(itp) == 'a'
        assert next(itp) == '_'
        assert next(itp) == 'e'
        assert next(itp) == '_'
        assert next(itp) == 'i'
        assert next(itp) == '_'
        assert next(itp) == 'o'
        assert next(itp) == '_'
        assert next(itp) == 'u'
        assert_raises(StopIteration, next, itp)

    def test_intersperse_empty(self):
        itp = intersperse(1, '')
        assert_raises(StopIteration, next, itp)

    def test_intersperse_not_iterable(self):
        itp = intersperse('x', 1)
        assert_raises(TypeError, next, itp)

    def test_intersperse_generator(self):
        itp = intersperse('x', range(5))
        assert next(itp) == 0
        assert next(itp) == 'x'
        assert next(itp) == 1


class UniqueToEachTests(TestCase):
    """Tests for ``unique_to_each()``"""

    def test_all_unique(self):
        """When all the input iterables are unique the output should match
        the input."""
        iterables = [[1, 2], [3, 4, 5], [6, 7, 8]]
        eq_(unique_to_each(*iterables), iterables)

    def test_duplicates(self):
        """When there are duplicates in any of the input iterables that aren't
        in the rest, those duplicates should be emitted."""
        iterables = ["mississippi", "missouri"]
        eq_(unique_to_each(*iterables), [['p', 'p'], ['o', 'u', 'r']])

    def test_mixed(self):
        """When the input iterables contain different types the function should
        still behave properly"""
        iterables = ['x', (i for i in range(3)), [1, 2, 3], tuple()]
        eq_(unique_to_each(*iterables), [['x'], [0], [3], []])


class WindowedTests(TestCase):
    """Tests for ``windowed()``"""

    def test_basic(self):
        actual = list(windowed([1, 2, 3, 4, 5], 3))
        expected = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
        eq_(actual, expected)

    def test_large_size(self):
        """
        When the window size is larger than the iterable, and no fill value is
        given,``None`` should be filled in.
        """
        actual = list(windowed([1, 2, 3, 4, 5], 6))
        expected = [(1, 2, 3, 4, 5, None)]
        eq_(actual, expected)

    def test_fillvalue(self):
        """
        When the window size is larger than the iterable, the given fill value
        should be used.
        """
        actual = list(windowed([1, 2, 3, 4, 5], 6, '!'))
        expected = [(1, 2, 3, 4, 5, '!')]
        eq_(actual, expected)

    def test_zero(self):
        """When the window size is zero, an empty tuple should be emitted."""
        actual = list(windowed([1, 2, 3, 4, 5], 0))
        expected = [tuple()]
        eq_(actual, expected)

    def test_negative(self):
        """When the window size is negative, ValueError should be raised."""
        with self.assertRaises(ValueError):
            list(windowed([1, 2, 3, 4, 5], -1))
