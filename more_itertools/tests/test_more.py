from __future__ import division, print_function, unicode_literals

from decimal import Decimal
from fractions import Fraction
from functools import reduce
from io import StringIO
from itertools import chain, count, groupby, permutations, product, repeat
from operator import itemgetter
from unittest import TestCase

from nose.tools import eq_, assert_raises
import six
from six.moves import filter, range, zip

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
        actual = sorted(
            reduce(list.__add__, [list(it) for it in iterables]), reverse=True
        )
        expected = list(collate(*iterables, key=lambda x: -x))
        eq_(actual, expected)

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

        # Negative indexing should work too
        eq_(p[-2], 'k')
        eq_(p[-9], 'd')
        self.assertRaises(IndexError, lambda: p[-10])

    def test_slicing(self):
        """Slicing the peekable shouldn't advance the iterator."""
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

    def test_slicing_reset(self):
        """Test slicing on a fresh iterable each time"""
        iterable = ['0', '1', '2', '3', '4', '5']
        indexes = list(range(-4, len(iterable) + 4)) + [None]
        steps = [1, 2, 3, 4, -1, -2, -3, 4]
        for slice_args in product(indexes, indexes, steps):
            it = iter(iterable)
            p = peekable(it)
            next(p)
            index = slice(*slice_args)
            actual = p[index]
            expected = iterable[1:][index]
            self.assertEqual(actual, expected, slice_args)

    def test_slicing_error(self):
        iterable = '01234567'
        p = peekable(iter(iterable))

        # Prime the cache
        p.peek()
        old_cache = list(p._cache)

        # Illegal slice
        with self.assertRaises(ValueError):
            p[1:-1:0]

        # Neither the cache nor the iteration should be affected
        self.assertEqual(old_cache, list(p._cache))
        self.assertEqual(list(p), list(iterable))

    def test_passthrough(self):
        """Iterating a peekable without using ``peek()`` or ``prepend()``
        should just give the underlying iterable's elements (a trivial test but
        useful to set a baseline in case something goes wrong)"""
        expected = [1, 2, 3, 4, 5]
        actual = list(peekable(expected))
        eq_(actual, expected)

    # prepend() behavior tests

    def test_prepend(self):
        """Tests intersperesed ``prepend()`` and ``next()`` calls"""
        it = peekable(range(2))
        actual = []

        # Test prepend() before next()
        it.prepend(10)
        actual += [next(it), next(it)]

        # Test prepend() between next()s
        it.prepend(11)
        actual += [next(it), next(it)]

        # Test prepend() after source iterable is consumed
        it.prepend(12)
        actual += [next(it)]

        expected = [10, 0, 11, 1, 12]
        eq_(actual, expected)

    def test_multi_prepend(self):
        """Tests prepending multiple items and getting them in proper order"""
        it = peekable(range(5))
        actual = [next(it), next(it)]
        it.prepend(10, 11, 12)
        it.prepend(20, 21)
        actual += list(it)
        expected = [0, 1, 20, 21, 10, 11, 12, 2, 3, 4]
        eq_(actual, expected)

    def test_empty(self):
        """Tests prepending in front of an empty iterable"""
        it = peekable([])
        it.prepend(10)
        actual = list(it)
        expected = [10]
        eq_(actual, expected)

    def test_prepend_truthiness(self):
        """Tests that ``__bool__()`` or ``__nonzero__()`` works properly
        with ``prepend()``"""
        it = peekable(range(5))
        self.assertTrue(it)
        actual = list(it)
        self.assertFalse(it)
        it.prepend(10)
        self.assertTrue(it)
        actual += [next(it)]
        self.assertFalse(it)
        expected = [0, 1, 2, 3, 4, 10]
        eq_(actual, expected)

    def test_multi_prepend_peek(self):
        """Tests prepending multiple elements and getting them in reverse order
        while peeking"""
        it = peekable(range(5))
        actual = [next(it), next(it)]
        eq_(it.peek(), 2)
        it.prepend(10, 11, 12)
        eq_(it.peek(), 10)
        it.prepend(20, 21)
        eq_(it.peek(), 20)
        actual += list(it)
        self.assertFalse(it)
        expected = [0, 1, 20, 21, 10, 11, 12, 2, 3, 4]
        eq_(actual, expected)

    def test_prepend_after_stop(self):
        """Test resuming iteration after a previous exhaustion"""
        it = peekable(range(3))
        eq_(list(it), [0, 1, 2])
        self.assertRaises(StopIteration, lambda: next(it))
        it.prepend(10)
        eq_(next(it), 10)
        self.assertRaises(StopIteration, lambda: next(it))

    def test_prepend_slicing(self):
        """Tests interaction between prepending and slicing"""
        seq = list(range(20))
        p = peekable(seq)

        p.prepend(30, 40, 50)
        pseq = [30, 40, 50] + seq  # pseq for prepended_seq

        # adapt the specific tests from test_slicing
        eq_(p[0], 30)
        eq_(p[1:8], pseq[1:8])
        eq_(p[1:], pseq[1:])
        eq_(p[:5], pseq[:5])
        eq_(p[:], pseq[:])
        eq_(p[:100], pseq[:100])
        eq_(p[::2], pseq[::2])
        eq_(p[::-1], pseq[::-1])

    def test_prepend_indexing(self):
        """Tests interaction between prepending and indexing"""
        seq = list(range(20))
        p = peekable(seq)

        p.prepend(30, 40, 50)

        eq_(p[0], 30)
        eq_(next(p), 30)
        eq_(p[2], 0)
        eq_(next(p), 40)
        eq_(p[0], 50)
        eq_(p[9], 8)
        eq_(next(p), 50)
        eq_(p[8], 8)
        eq_(p[-2], 18)
        eq_(p[-9], 11)
        self.assertRaises(IndexError, lambda: p[-21])

    def test_prepend_iterable(self):
        """Tests prepending from an iterable"""
        it = peekable(range(5))
        # Don't directly use the range() object to avoid any range-specific
        # optimizations
        it.prepend(*(x for x in range(5)))
        actual = list(it)
        expected = list(chain(range(5), range(5)))
        eq_(actual, expected)

    def test_prepend_many(self):
        """Tests that prepending a huge number of elements works"""
        it = peekable(range(5))
        # Don't directly use the range() object to avoid any range-specific
        # optimizations
        it.prepend(*(x for x in range(20000)))
        actual = list(it)
        expected = list(chain(range(20000), range(5)))
        eq_(actual, expected)

    def test_prepend_reversed(self):
        """Tests prepending from a reversed iterable"""
        it = peekable(range(3))
        it.prepend(*reversed((10, 11, 12)))
        actual = list(it)
        expected = [12, 11, 10, 0, 1, 2]
        eq_(actual, expected)


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
    """Sanity-checks for ``ilen()``."""
    # Non-empty
    eq_(ilen(filter(lambda x: x % 10 == 0, range(101))), 11)

    # Empty
    eq_(ilen((x for x in range(0))), 0)

    # Iterable with __len__
    eq_(ilen(list(range(6))), 6)


def test_with_iter():
    """Make sure ``with_iter`` iterates over and closes things correctly."""
    s = StringIO('One fish\nTwo fish')
    initial_words = [line.split()[0] for line in with_iter(s)]

    # Iterable's items should be faithfully represented
    eq_(initial_words, ['One', 'Two'])
    # The file object should be closed
    eq_(s.closed, True)


def test_one():
    """Test the ``one()`` cases that aren't covered by its doctests."""
    # Infinite iterables
    numbers = count()
    assert_raises(ValueError, one, numbers)  # burn 0 and 1
    eq_(next(numbers), 2)


class IntersperseTest(TestCase):
    """ Tests for intersperse() """

    def test_even(self):
        eq_(list(intersperse(None, '01')), ['0', None, '1'])

    def test_odd(self):
        eq_(list(intersperse(None, '012')), ['0', None, '1', None, '2'])

    def test_generator(self):
        iterable = (x for x in '012')
        eq_(list(intersperse(None, iterable)), ['0', None, '1', None, '2'])

    def test_intersperse_not_iterable(self):
        assert_raises(TypeError, lambda: intersperse('x', 1))


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
        When sizes don't match evenly, the given fill value should be used.
        """
        iterable = [1, 2, 3, 4, 5]

        for n, kwargs, expected in [
            (6, {}, [(1, 2, 3, 4, 5, '!')]),  # n > len(iterable)
            (3, {'step': 3}, [(1, 2, 3), (4, 5, '!')]),  # using ``step``
        ]:
            actual = list(windowed(iterable, n, fillvalue='!', **kwargs))
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

    def test_step(self):
        """The window should advance by the number of steps provided"""
        iterable = [1, 2, 3, 4, 5, 6, 7]
        for n, step, expected in [
            (3, 2, [(1, 2, 3), (3, 4, 5), (5, 6, 7)]),  # n > step
            (3, 3, [(1, 2, 3), (4, 5, 6), (7, None, None)]),  # n == step
            (3, 4, [(1, 2, 3), (5, 6, 7)]),  # line up nicely
            (3, 5, [(1, 2, 3), (6, 7, None)]),  # off by one
            (3, 6, [(1, 2, 3), (7, None, None)]),  # off by two
            (3, 7, [(1, 2, 3)]),  # step past the end
            (7, 8, [(1, 2, 3, 4, 5, 6, 7)]),  # step > len(iterable)
        ]:
            actual = list(windowed(iterable, n, step=step))
            eq_(actual, expected)

        # Step must be greater than or equal to 1
        with self.assertRaises(ValueError):
            list(windowed(iterable, 3, step=0))


class BucketTests(TestCase):
    """Tests for ``bucket()``"""

    def test_basic(self):
        iterable = [10, 20, 30, 11, 21, 31, 12, 22, 23, 33]
        D = bucket(iterable, key=lambda x: 10 * (x // 10))

        # In-order access
        eq_(list(D[10]), [10, 11, 12])

        # Out of order access
        eq_(list(D[30]), [30, 31, 33])
        eq_(list(D[20]), [20, 21, 22, 23])

        eq_(list(D[40]), [])  # Nothing in here!

    def test_in(self):
        iterable = [10, 20, 30, 11, 21, 31, 12, 22, 23, 33]
        D = bucket(iterable, key=lambda x: 10 * (x // 10))

        self.assertTrue(10 in D)
        self.assertFalse(40 in D)
        self.assertTrue(20 in D)
        self.assertFalse(21 in D)

        # Checking in-ness shouldn't advance the iterator
        eq_(next(D[10]), 10)


class SpyTests(TestCase):
    """Tests for ``spy()``"""

    def test_basic(self):
        original_iterable = iter('abcdefg')
        head, new_iterable = spy(original_iterable)
        eq_(head, ['a'])
        eq_(list(new_iterable), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    def test_unpacking(self):
        original_iterable = iter('abcdefg')
        (first, second, third), new_iterable = spy(original_iterable, 3)
        eq_(first, 'a')
        eq_(second, 'b')
        eq_(third, 'c')
        eq_(list(new_iterable), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    def test_too_many(self):
        original_iterable = iter('abc')
        head, new_iterable = spy(original_iterable, 4)
        eq_(head, ['a', 'b', 'c'])
        eq_(list(new_iterable), ['a', 'b', 'c'])

    def test_zero(self):
        original_iterable = iter('abc')
        head, new_iterable = spy(original_iterable, 0)
        eq_(head, [])
        eq_(list(new_iterable), ['a', 'b', 'c'])


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
    """Tests for ``collapse()``"""

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
        l = (1, [2], (3, [4, (5,)], 'ab'))
        actual = list(collapse(l, base_type=list))
        expected = [1, [2], 3, [4, (5,)], 'ab']
        eq_(actual, expected)


class SideEffectTests(TestCase):
    """Tests for ``side_effect()``"""

    def test_individual(self):
        # The function increments the counter for each call
        counter = [0]

        def func(arg):
            counter[0] += 1

        result = list(side_effect(func, range(10)))
        eq_(result, list(range(10)))
        eq_(counter[0], 10)

    def test_chunked(self):
        # The function increments the counter for each call
        counter = [0]

        def func(arg):
            counter[0] += 1

        result = list(side_effect(func, range(10), 2))
        eq_(result, list(range(10)))
        eq_(counter[0], 5)

    def test_before_after(self):
        f = StringIO()
        collector = []

        def func(item):
            print(item, file=f)
            collector.append(f.getvalue())

        def it():
            yield u'a'
            yield u'b'
            raise Exception('kaboom')

        before = lambda: print('HEADER', file=f)
        after = f.close

        try:
            consume(side_effect(func, it(), before=before, after=after))
        except Exception:
            pass

        # The iterable should have been written to the file
        self.assertEqual(collector, [u'HEADER\na\n', u'HEADER\na\nb\n'])

        # The file should be closed even though something bad happened
        self.assertTrue(f.closed)

    def test_before_fails(self):
        f = StringIO()
        func = lambda x: print(x, file=f)

        def before():
            raise Exception('ouch')

        try:
            consume(side_effect(func, u'abc', before=before, after=f.close))
        except Exception:
            pass

        # The file should be closed even though something bad happened in the
        # before function
        self.assertTrue(f.closed)


class SlicedTests(TestCase):
    """Tests for ``sliced()``"""

    def test_even(self):
        """Test when the length of the sequence is divisible by *n*"""
        seq = 'ABCDEFGHI'
        eq_(list(sliced(seq, 3)), ['ABC', 'DEF', 'GHI'])

    def test_odd(self):
        """Test when the length of the sequence is not divisible by *n*"""
        seq = 'ABCDEFGHI'
        eq_(list(sliced(seq, 4)), ['ABCD', 'EFGH', 'I'])

    def test_not_sliceable(self):
        seq = (x for x in 'ABCDEFGHI')

        with self.assertRaises(TypeError):
            list(sliced(seq, 3))


class SplitBeforeTest(TestCase):
    """Tests for ``split_before()``"""

    def test_starts_with_sep(self):
        actual = list(split_before('xooxoo', lambda c: c == 'x'))
        expected = [['x', 'o', 'o'], ['x', 'o', 'o']]
        eq_(actual, expected)

    def test_ends_with_sep(self):
        actual = list(split_before('ooxoox', lambda c: c == 'x'))
        expected = [['o', 'o'], ['x', 'o', 'o'], ['x']]
        eq_(actual, expected)

    def test_no_sep(self):
        actual = list(split_before('ooo', lambda c: c == 'x'))
        expected = [['o', 'o', 'o']]
        eq_(actual, expected)


class SplitAfterTest(TestCase):
    """Tests for ``split_after()``"""

    def test_starts_with_sep(self):
        actual = list(split_after('xooxoo', lambda c: c == 'x'))
        expected = [['x'], ['o', 'o', 'x'], ['o', 'o']]
        eq_(actual, expected)

    def test_ends_with_sep(self):
        actual = list(split_after('ooxoox', lambda c: c == 'x'))
        expected = [['o', 'o', 'x'], ['o', 'o', 'x']]
        eq_(actual, expected)

    def test_no_sep(self):
        actual = list(split_after('ooo', lambda c: c == 'x'))
        expected = [['o', 'o', 'o']]
        eq_(actual, expected)


class PaddedTest(TestCase):
    """Tests for ``padded()``"""

    def test_no_n(self):
        seq = [1, 2, 3]

        # No fillvalue
        self.assertEqual(take(5, padded(seq)), [1, 2, 3, None, None])

        # With fillvalue
        self.assertEqual(take(5, padded(seq, fillvalue='')), [1, 2, 3, '', ''])

    def test_invalid_n(self):
        self.assertRaises(ValueError, lambda: list(padded([1, 2, 3], n=-1)))
        self.assertRaises(ValueError, lambda: list(padded([1, 2, 3], n=0)))

    def test_valid_n(self):
        seq = [1, 2, 3, 4, 5]

        # No need for padding: len(seq) <= n
        self.assertEqual(list(padded(seq, n=4)), [1, 2, 3, 4, 5])
        self.assertEqual(list(padded(seq, n=5)), [1, 2, 3, 4, 5])

        # No fillvalue
        self.assertEqual(list(padded(seq, n=7)), [1, 2, 3, 4, 5, None, None])

        # With fillvalue
        self.assertEqual(
            list(padded(seq, fillvalue='', n=7)), [1, 2, 3, 4, 5, '', '']
        )

    def test_next_multiple(self):
        seq = [1, 2, 3, 4, 5, 6]

        # No need for padding: len(seq) % n == 0
        self.assertEqual(
            list(padded(seq, n=3, next_multiple=True)), [1, 2, 3, 4, 5, 6]
        )

        # Padding needed: len(seq) < n
        self.assertEqual(
            list(padded(seq, n=8, next_multiple=True)),
            [1, 2, 3, 4, 5, 6, None, None]
        )

        # No padding needed: len(seq) == n
        self.assertEqual(
            list(padded(seq, n=6, next_multiple=True)), [1, 2, 3, 4, 5, 6]
        )

        # Padding needed: len(seq) > n
        self.assertEqual(
            list(padded(seq, n=4, next_multiple=True)),
            [1, 2, 3, 4, 5, 6, None, None]
        )

        # With fillvalue
        self.assertEqual(
            list(padded(seq, fillvalue='', n=4, next_multiple=True)),
            [1, 2, 3, 4, 5, 6, '', '']
        )


class DistributeTest(TestCase):
    """Tests for distribute()"""

    def test_invalid_n(self):
        self.assertRaises(ValueError, lambda: distribute(-1, [1, 2, 3]))
        self.assertRaises(ValueError, lambda: distribute(0, [1, 2, 3]))

    def test_basic(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for n, expected in [
            (1, [iterable]),
            (2, [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]),
            (3, [[1, 4, 7, 10], [2, 5, 8], [3, 6, 9]]),
            (10, [[n] for n in range(1, 10 + 1)]),
        ]:
            eq_([list(x) for x in distribute(n, iterable)], expected)

    def test_large_n(self):
        iterable = [1, 2, 3, 4]
        eq_(
            [list(x) for x in distribute(6, iterable)],
            [[1], [2], [3], [4], [], []]
        )


class StaggerTest(TestCase):
    """Tests for ``stagger()``"""

    def test_default(self):
        iterable = [0, 1, 2, 3]
        actual = list(stagger(iterable))
        expected = [(None, 0, 1), (0, 1, 2), (1, 2, 3)]
        eq_(actual, expected)

    def test_offsets(self):
        iterable = [0, 1, 2, 3]
        for offsets, expected in [
            ((-2, 0, 2), [('', 0, 2), ('', 1, 3)]),
            ((-2, -1), [('', ''), ('', 0), (0, 1), (1, 2), (2, 3)]),
            ((1, 2), [(1, 2), (2, 3)]),
        ]:
            all_groups = stagger(iterable, offsets=offsets, fillvalue='')
            eq_(list(all_groups), expected)

    def test_longest(self):
        iterable = [0, 1, 2, 3]
        for offsets, expected in [
            (
                (-1, 0, 1),
                [('', 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, ''), (3, '', '')]
            ),
            ((-2, -1), [('', ''), ('', 0), (0, 1), (1, 2), (2, 3), (3, '')]),
            ((1, 2), [(1, 2), (2, 3), (3, '')]),
        ]:
            all_groups = stagger(
                iterable, offsets=offsets, fillvalue='', longest=True
            )
            eq_(list(all_groups), expected)


class ZipOffsetTest(TestCase):
    """Tests for ``zip_offset()``"""

    def test_shortest(self):
        seq_1 = [0, 1, 2, 3]
        seq_2 = [0, 1, 2, 3, 4, 5]
        seq_3 = [0, 1, 2, 3, 4, 5, 6, 7]
        actual = list(
            zip_offset(seq_1, seq_2, seq_3, offsets=(-1, 0, 1), fillvalue='')
        )
        expected = [('', 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]
        eq_(actual, expected)

    def test_longest(self):
        seq_1 = [0, 1, 2, 3]
        seq_2 = [0, 1, 2, 3, 4, 5]
        seq_3 = [0, 1, 2, 3, 4, 5, 6, 7]
        actual = list(
            zip_offset(seq_1, seq_2, seq_3, offsets=(-1, 0, 1), longest=True)
        )
        expected = [
            (None, 0, 1),
            (0, 1, 2),
            (1, 2, 3),
            (2, 3, 4),
            (3, 4, 5),
            (None, 5, 6),
            (None, None, 7),
        ]
        eq_(actual, expected)

    def test_mismatch(self):
        iterables = [0, 1, 2], [2, 3, 4]
        offsets = (-1, 0, 1)
        self.assertRaises(
            ValueError, lambda: list(zip_offset(*iterables, offsets=offsets))
        )


class SortTogetherTest(TestCase):
    """Tests for sort_together()"""

    def test_key_list(self):
        """tests `key_list` including default, iterables include duplicates"""
        iterables = [['GA', 'GA', 'GA', 'CT', 'CT', 'CT'],
                     ['May', 'Aug.', 'May', 'June', 'July', 'July'],
                     [97, 20, 100, 70, 100, 20]]

        eq_(sort_together(iterables),
            [('CT', 'CT', 'CT', 'GA', 'GA', 'GA'),
             ('June', 'July', 'July', 'May', 'Aug.', 'May'),
             (70, 100, 20, 97, 20, 100)])

        eq_(sort_together(iterables, key_list=(0, 1)),
            [('CT', 'CT', 'CT', 'GA', 'GA', 'GA'),
             ('July', 'July', 'June', 'Aug.', 'May', 'May'),
             (100, 20, 70, 20, 97, 100)])

        eq_(sort_together(iterables, key_list=(0, 1, 2)),
            [('CT', 'CT', 'CT', 'GA', 'GA', 'GA'),
             ('July', 'July', 'June', 'Aug.', 'May', 'May'),
             (20, 100, 70, 20, 97, 100)])

        eq_(sort_together(iterables, key_list=(2,)),
            [('GA', 'CT', 'CT', 'GA', 'GA', 'CT'),
             ('Aug.', 'July', 'June', 'May', 'May', 'July'),
             (20, 20, 70, 97, 100, 100)])

    def test_invalid_key_list(self):
        """tests `key_list` for indexes not available in `iterables`"""
        iterables = [['GA', 'GA', 'GA', 'CT', 'CT', 'CT'],
                     ['May', 'Aug.', 'May', 'June', 'July', 'July'],
                     [97, 20, 100, 70, 100, 20]]

        self.assertRaises(IndexError,
                          lambda: sort_together(iterables, key_list=(5,)))

    def test_reverse(self):
        """tests `reverse` to ensure a reverse sort for `key_list` iterables"""
        iterables = [['GA', 'GA', 'GA', 'CT', 'CT', 'CT'],
                     ['May', 'Aug.', 'May', 'June', 'July', 'July'],
                     [97, 20, 100, 70, 100, 20]]

        eq_(sort_together(iterables, key_list=(0, 1, 2), reverse=True),
            [('GA', 'GA', 'GA', 'CT', 'CT', 'CT'),
             ('May', 'May', 'Aug.', 'June', 'July', 'July'),
             (100, 97, 20, 70, 100, 20)])

    def test_uneven_iterables(self):
        """tests trimming of iterables to the shortest length before sorting"""
        iterables = [['GA', 'GA', 'GA', 'CT', 'CT', 'CT', 'MA'],
                     ['May', 'Aug.', 'May', 'June', 'July', 'July'],
                     [97, 20, 100, 70, 100, 20, 0]]

        eq_(sort_together(iterables),
            [('CT', 'CT', 'CT', 'GA', 'GA', 'GA'),
             ('June', 'July', 'July', 'May', 'Aug.', 'May'),
             (70, 100, 20, 97, 20, 100)])


class DivideTest(TestCase):
    """Tests for divide()"""

    def test_invalid_n(self):
        self.assertRaises(ValueError, lambda: divide(-1, [1, 2, 3]))
        self.assertRaises(ValueError, lambda: divide(0, [1, 2, 3]))

    def test_basic(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for n, expected in [
            (1, [iterable]),
            (2, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
            (3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
            (10, [[n] for n in range(1, 10 + 1)]),
        ]:
            eq_([list(x) for x in divide(n, iterable)], expected)

    def test_large_n(self):
        iterable = [1, 2, 3, 4]
        eq_(
            [list(x) for x in divide(6, iterable)],
            [[1], [2], [3], [4], [], []]
        )


class TestAlwaysIterable(TestCase):
    """Tests for always_iterable()"""
    def test_single(self):
        self.assertEqual(always_iterable(1), (1,))
        self.assertEqual(list(always_iterable(1)), [1])

    def test_strings(self):
        self.assertEqual(always_iterable('foo'), ('foo',))
        self.assertEqual(always_iterable(six.b('bar')), (six.b('bar'),))
        self.assertEqual(always_iterable(six.u(b'baz')), (six.u(b'baz'),))

    def test_iterables(self):
        self.assertEqual(always_iterable([0, 1]), [0, 1])
        self.assertEqual(list(iter('foo')), ['f', 'o', 'o'])
        self.assertEqual(list([]), [])

    def test_none(self):
        self.assertEqual(always_iterable(None), ())
        self.assertEqual(list(always_iterable(None)), [])

    def test_generator(self):
        def _gen():
            yield 0
            yield 1

        self.assertEqual(list(always_iterable(_gen())), [0, 1])


class AdjacentTests(TestCase):
    def test_typical(self):
        actual = list(adjacent(lambda x: x % 5 == 0, range(10)))
        expected = [(True, 0), (True, 1), (False, 2), (False, 3), (True, 4),
                    (True, 5), (True, 6), (False, 7), (False, 8), (False, 9)]
        self.assertEqual(actual, expected)

    def test_empty_iterable(self):
        actual = list(adjacent(lambda x: x % 5 == 0, []))
        expected = []
        self.assertEqual(actual, expected)

    def test_length_one(self):
        actual = list(adjacent(lambda x: x % 5 == 0, [0]))
        expected = [(True, 0)]
        self.assertEqual(actual, expected)

        actual = list(adjacent(lambda x: x % 5 == 0, [1]))
        expected = [(False, 1)]
        self.assertEqual(actual, expected)

    def test_consecutive_true(self):
        """Test that when the predicate matches multiple consecutive elements
        it doesn't repeat elements in the output"""
        actual = list(adjacent(lambda x: x % 5 < 2, range(10)))
        expected = [(True, 0), (True, 1), (True, 2), (False, 3), (True, 4),
                    (True, 5), (True, 6), (True, 7), (False, 8), (False, 9)]
        self.assertEqual(actual, expected)

    def test_distance(self):
        actual = list(adjacent(lambda x: x % 5 == 0, range(10), distance=2))
        expected = [(True, 0), (True, 1), (True, 2), (True, 3), (True, 4),
                    (True, 5), (True, 6), (True, 7), (False, 8), (False, 9)]
        self.assertEqual(actual, expected)

        actual = list(adjacent(lambda x: x % 5 == 0, range(10), distance=3))
        expected = [(True, 0), (True, 1), (True, 2), (True, 3), (True, 4),
                    (True, 5), (True, 6), (True, 7), (True, 8), (False, 9)]
        self.assertEqual(actual, expected)

    def test_large_distance(self):
        """Test distance larger than the length of the iterable"""
        iterable = range(10)
        actual = list(adjacent(lambda x: x % 5 == 4, iterable, distance=20))
        expected = list(zip(repeat(True), iterable))
        self.assertEqual(actual, expected)

        actual = list(adjacent(lambda x: False, iterable, distance=20))
        expected = list(zip(repeat(False), iterable))
        self.assertEqual(actual, expected)

    def test_zero_distance(self):
        """Test that adjacent() reduces to zip+map when distance is 0"""
        iterable = range(1000)
        predicate = lambda x: x % 4 == 2
        actual = adjacent(predicate, iterable, 0)
        expected = zip(map(predicate, iterable), iterable)
        self.assertTrue(all(a == e for a, e in zip(actual, expected)))

    def test_negative_distance(self):
        """Test that adjacent() raises an error with negative distance"""
        pred = lambda x: x
        self.assertRaises(ValueError, lambda: adjacent(pred, range(1000), -1))
        self.assertRaises(ValueError, lambda: adjacent(pred, range(10), -10))

    def test_grouping(self):
        """Test interaction of adjacent() with groupby_transform()"""
        iterable = adjacent(lambda x: x % 5 == 0, range(10))
        grouper = groupby_transform(iterable, itemgetter(0), itemgetter(1))
        actual = [(k, list(g)) for k, g in grouper]
        expected = [
            (True, [0, 1]),
            (False, [2, 3]),
            (True, [4, 5, 6]),
            (False, [7, 8, 9]),
        ]
        self.assertEqual(actual, expected)

    def test_call_once(self):
        """Test that the predicate is only called once per item."""
        already_seen = set()
        iterable = range(10)

        def predicate(item):
            self.assertNotIn(item, already_seen)
            already_seen.add(item)
            return True

        actual = list(adjacent(predicate, iterable))
        expected = [(True, x) for x in iterable]
        self.assertEqual(actual, expected)


class GroupByTransformTests(TestCase):
    def assertAllGroupsEqual(self, groupby1, groupby2):
        """Compare two groupby objects for equality, both keys and groups."""
        for a, b in zip(groupby1, groupby2):
            key1, group1 = a
            key2, group2 = b
            self.assertEqual(key1, key2)
            self.assertListEqual(list(group1), list(group2))
        self.assertRaises(StopIteration, lambda: next(groupby1))
        self.assertRaises(StopIteration, lambda: next(groupby2))

    def test_default_funcs(self):
        """Test that groupby_transform() with default args mimics groupby()"""
        iterable = [(x // 5, x) for x in range(1000)]
        actual = groupby_transform(iterable)
        expected = groupby(iterable)
        self.assertAllGroupsEqual(actual, expected)

    def test_valuefunc(self):
        iterable = [(int(x / 5), int(x / 3), x) for x in range(10)]

        # Test the standard usage of grouping one iterable using another's keys
        grouper = groupby_transform(
            iterable, keyfunc=itemgetter(0), valuefunc=itemgetter(-1)
        )
        actual = [(k, list(g)) for k, g in grouper]
        expected = [(0, [0, 1, 2, 3, 4]), (1, [5, 6, 7, 8, 9])]
        self.assertEqual(actual, expected)

        grouper = groupby_transform(
            iterable, keyfunc=itemgetter(1), valuefunc=itemgetter(-1)
        )
        actual = [(k, list(g)) for k, g in grouper]
        expected = [(0, [0, 1, 2]), (1, [3, 4, 5]), (2, [6, 7, 8]), (3, [9])]
        self.assertEqual(actual, expected)

        # and now for something a little different
        d = dict(zip(range(10), 'abcdefghij'))
        grouper = groupby_transform(
            range(10), keyfunc=lambda x: x // 5, valuefunc=d.get
        )
        actual = [(k, ''.join(g)) for k, g in grouper]
        expected = [(0, 'abcde'), (1, 'fghij')]
        self.assertEqual(actual, expected)

    def test_no_valuefunc(self):
        iterable = range(1000)

        def key(x):
            return x // 5

        actual = groupby_transform(iterable, key, valuefunc=None)
        expected = groupby(iterable, key)
        self.assertAllGroupsEqual(actual, expected)

        actual = groupby_transform(iterable, key)  # default valuefunc
        expected = groupby(iterable, key)
        self.assertAllGroupsEqual(actual, expected)


class ArithmeticSequenceTests(TestCase):
    def test_basic(self):
        for args, expected in [
            ((4,), [0, 1, 2, 3]),
            ((4.0,), [0.0, 1.0, 2.0, 3.0]),
            ((1.0, 4), [1.0, 2.0, 3.0]),
            ((1, 4.0), [1, 2, 3]),
            ((1.0, 5), [1.0, 2.0, 3.0, 4.0]),
            ((0, 20, 5), [0, 5, 10, 15]),
            ((0, 20, 5.0), [0.0, 5.0, 10.0, 15.0]),
            ((0, 10, 3), [0, 3, 6, 9]),
            ((0, 10, 3.0), [0.0, 3.0, 6.0, 9.0]),
            ((0, -5, -1), [0, -1, -2, -3, -4]),
            ((0.0, -5, -1), [0.0, -1.0, -2.0, -3.0, -4.0]),
            ((1, 2, Fraction(1, 2)), [Fraction(1, 1), Fraction(3, 2)]),
            ((0,), []),
            ((0.0,), []),
            ((1, 0), []),
            ((1.0, 0.0), []),
            ((Fraction(2, 1),), [Fraction(0, 1), Fraction(1, 1)]),
            ((Decimal('2.0'),), [Decimal('0.0'), Decimal('1.0')]),
        ]:
            actual = list(numeric_range(*args))
            self.assertEqual(actual, expected)
            self.assertTrue(
                all(type(a) == type(e) for a, e in zip(actual, expected))
            )

    def test_arg_count(self):
        self.assertRaises(TypeError, lambda: list(numeric_range()))
        self.assertRaises(
            TypeError, lambda: list(numeric_range(0, 1, 2, 3))
        )

    def test_zero_step(self):
        self.assertRaises(
            ValueError, lambda: list(numeric_range(1, 2, 0))
        )


class CountCycleTests(TestCase):
    def test_basic(self):
        expected = [
            (0, 'a'), (0, 'b'), (0, 'c'),
            (1, 'a'), (1, 'b'), (1, 'c'),
            (2, 'a'), (2, 'b'), (2, 'c'),
        ]
        for actual in [
            take(9, count_cycle('abc')),  # n=None
            list(count_cycle('abc', 3)),  # n=3
        ]:
            self.assertEqual(actual, expected)

    def test_empty(self):
        self.assertEqual(list(count_cycle('')), [])
        self.assertEqual(list(count_cycle('', 2)), [])

    def test_negative(self):
        self.assertEqual(list(count_cycle('abc', -3)), [])


class LocateTests(TestCase):
    def test_default_pred(self):
        iterable = [0, 1, 1, 0, 1, 0, 0]
        actual = list(locate(iterable))
        expected = [1, 2, 4]
        self.assertEqual(actual, expected)

    def test_no_matches(self):
        iterable = [0, 0, 0]
        actual = list(locate(iterable))
        expected = []
        self.assertEqual(actual, expected)

    def test_custom_pred(self):
        iterable = ['0', 1, 1, '0', 1, '0', '0']
        pred = lambda x: x == '0'
        actual = list(locate(iterable, pred))
        expected = [0, 3, 5, 6]
        self.assertEqual(actual, expected)


class StripFunctionTests(TestCase):
    def test_hashable(self):
        iterable = list('www.example.com')
        pred = lambda x: x in set('cmowz.')

        self.assertEqual(list(lstrip(iterable, pred)), list('example.com'))
        self.assertEqual(list(rstrip(iterable, pred)), list('www.example'))
        self.assertEqual(list(strip(iterable, pred)), list('example'))

    def test_not_hashable(self):
        iterable = [
            list('http://'), list('www'), list('.example'), list('.com')
        ]
        pred = lambda x: x in [list('http://'), list('www'), list('.com')]

        self.assertEqual(list(lstrip(iterable, pred)), iterable[2:])
        self.assertEqual(list(rstrip(iterable, pred)), iterable[:3])
        self.assertEqual(list(strip(iterable, pred)), iterable[2: 3])

    def test_math(self):
        iterable = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2]
        pred = lambda x: x <= 2

        self.assertEqual(list(lstrip(iterable, pred)), iterable[3:])
        self.assertEqual(list(rstrip(iterable, pred)), iterable[:-3])
        self.assertEqual(list(strip(iterable, pred)), iterable[3:-3])


class IsliceExtendedTests(TestCase):
    def test_all(self):
        iterable = ['0', '1', '2', '3', '4', '5']
        indexes = list(range(-4, len(iterable) + 4)) + [None]
        steps = [1, 2, 3, 4, -1, -2, -3, 4]
        for slice_args in product(indexes, indexes, steps):
            try:
                actual = list(islice_extended(iterable, *slice_args))
            except Exception as e:
                self.fail((slice_args, e))

            expected = iterable[slice(*slice_args)]
            self.assertEqual(actual, expected, slice_args)

    def test_zero_step(self):
        with self.assertRaises(ValueError):
            list(islice_extended([1, 2, 3], 0, 1, 0))
