from contextlib import closing
from itertools import count, islice, ifilter, permutations
from StringIO import StringIO
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
    eq_(ilen(ifilter(lambda x: x % 10 == 0, range(101))), 11)


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
        itp = intersperse('x', xrange(5))
        assert next(itp) == 0
        assert next(itp) == 'x'
        assert next(itp) == 1


class EmptyIteratorTests(TestCase):
    """Tests for ``empty_iterator()``"""

    def test_empty(self):
        eq_(list(empty_iterator()), [])

    def test_raises_stopiteration(self):
        assert_raises(StopIteration, next, empty_iterator())
