from itertools import repeat
from random import seed
from unittest import TestCase

from nose.tools import eq_, assert_raises, ok_

from more_itertools import *


def setup_module():
    seed(1337)


class TakeTests(TestCase):
    """Tests for ``take()``"""

    def test_simple_take(self):
        """Test basic usage"""
        t = take(5, xrange(10))
        eq_(t, [0, 1, 2, 3, 4])

    def test_null_take(self):
        """Check the null case"""
        t = take(0, xrange(10))
        eq_(t, [])

    def test_negative_take(self):
        """Make sure taking negative items results in a ValueError"""
        assert_raises(ValueError, take, -3, xrange(10))

    def test_take_too_much(self):
        """Taking more than an iterator has remaining should return what the
        iterator has remaining.

        """
        t = take(10, xrange(5))
        eq_(t, [0, 1, 2, 3, 4])


class TabulateTests(TestCase):
    """Tests for ``tabulate()``"""

    def test_simple_tabulate(self):
        """Test the happy path"""
        t = tabulate(lambda x: x)
        f = tuple([next(t) for _ in range(3)])
        eq_(f, (0, 1, 2))

    def test_count(self):
        """Ensure tabulate accepts specific count"""
        t = tabulate(lambda x: 2 * x, -1)
        f = (next(t), next(t), next(t))
        eq_(f, (-2, 0, 2))


class ConsumeTests(TestCase):
    """Tests for ``consume()``"""

    def test_sanity(self):
        """Test basic functionality"""
        r = (x for x in range(10))
        consume(r, 3)
        eq_(3, next(r))

    def test_null_consume(self):
        """Check the null case"""
        r = (x for x in range(10))
        consume(r, 0)
        eq_(0, next(r))

    def test_negative_consume(self):
        """Check that negative consumsion throws an error"""
        r = (x for x in range(10))
        assert_raises(ValueError, consume, r, -1)

    def test_total_consume(self):
        """Check that iterator is totally consumed by default"""
        r = (x for x in range(10))
        consume(r)
        assert_raises(StopIteration, next, r)


class NthTests(TestCase):
    """Tests for ``nth()``"""

    def test_basic(self):
        """Make sure the nth item is returned"""
        l = range(10)
        for i, v in enumerate(l):
            eq_(nth(l, i), v)

    def test_default(self):
        """Ensure a default value is returned when nth item not found"""
        l = range(3)
        eq_(nth(l, 100, "zebra"), "zebra")

    def test_negative_item_raises(self):
        """Ensure asking for a negative item raises an exception"""
        assert_raises(ValueError, nth, range(10), -3)


class QuantifyTests(TestCase):
    """Tests for ``quantify()``"""

    def test_happy_path(self):
        """Make sure True count is returned"""
        q = [True, False, True]
        eq_(quantify(q), 2)

    def test_custom_predicate(self):
        """Ensure non-default predicates return as expected"""
        q = range(10)
        eq_(quantify(q, lambda x: x % 2 == 0), 5)


class PadnoneTests(TestCase):
    """Tests for ``padnone()``"""

    def test_happy_path(self):
        """wrapper iterator should return None indefinitely"""
        r = range(2)
        p = padnone(r)
        eq_([0, 1, None, None], [next(p) for _ in range(4)])


class NcyclesTests(TestCase):
    """Tests for ``nyclces()``"""

    def test_happy_path(self):
        """cycle a sequence three times"""
        r = ["a", "b", "c"]
        n = ncycles(r, 3)
        eq_(["a", "b", "c", "a", "b", "c", "a", "b", "c"],
            list(n))

    def test_null_case(self):
        """asking for 0 cycles should return an empty iterator"""
        n = ncycles(range(100), 0)
        assert_raises(StopIteration, next, n)

    def test_pathalogical_case(self):
        """asking for negative cycles should return an empty iterator"""
        n = ncycles(range(100), -10)
        assert_raises(StopIteration, next, n)


class DotproductTests(TestCase):
    """Tests for ``dotproduct()``'"""

    def test_happy_path(self):
        """simple dotproduct example"""
        eq_(400, dotproduct([10, 10], [20, 20]))


class FlattenTests(TestCase):
    """Tests for ``flatten()``"""

    def test_basic_usage(self):
        """ensure list of lists is flattened one level"""
        f = [[0, 1, 2], [3, 4, 5]]
        eq_(range(6), list(flatten(f)))

    def test_single_level(self):
        """ensure list of lists is flattened only one level"""
        f = [[0, [1, 2]], [[3, 4], 5]]
        eq_([0, [1, 2], [3, 4], 5], list(flatten(f)))


class RepeatfuncTests(TestCase):
    """Tests for ``repeatfunc()``"""

    def test_simple_repeat(self):
        """test simple repeated functions"""
        r = repeatfunc(lambda: 5)
        eq_([5, 5, 5, 5, 5], [next(r) for _ in range(5)])

    def test_finite_repeat(self):
        """ensure limited repeat when times is provided"""
        r = repeatfunc(lambda: 5, times=5)
        eq_([5, 5, 5, 5, 5], list(r))

    def test_added_arguments(self):
        """ensure arguments are applied to the function"""
        r = repeatfunc(lambda x: x, 2, 3)
        eq_([3, 3], list(r))

    def test_null_times(self):
        """repeat 0 should return an empty iterator"""
        r = repeatfunc(range, 0, 3)
        assert_raises(StopIteration, next, r)


class PairwiseTests(TestCase):
    """Tests for ``pairwise()``"""

    def test_base_case(self):
        """ensure an iterable will return pairwise"""
        p = pairwise([1, 2, 3])
        eq_([(1, 2), (2, 3)], list(p))

    def test_short_case(self):
        """ensure an empty iterator if there's not enough values to pair"""
        p = pairwise("a")
        assert_raises(StopIteration, next, p)


class GrouperTests(TestCase):
    """Tests for ``grouper()``"""

    def test_even(self):
        """Test when group size divides evenly into the length of
        the iterable.

        """
        eq_(list(grouper(3, 'ABCDEF')), [('A', 'B', 'C'), ('D', 'E', 'F')])

    def test_odd(self):
        """Test when group size does not divide evenly into the length of the
        iterable.

        """
        eq_(list(grouper(3, 'ABCDE')), [('A', 'B', 'C'), ('D', 'E', None)])

    def test_fill_value(self):
        """Test that the fill value is used to pad the final group"""
        eq_(list(grouper(3, 'ABCDE', 'x')), [('A', 'B', 'C'), ('D', 'E', 'x')])


class RoundrobinTests(TestCase):
    """Tests for ``roundrobin()``"""

    def test_even_groups(self):
        """Ensure ordered output from evenly populated iterables"""
        eq_(list(roundrobin('ABC', [1, 2, 3], range(3))),
            ['A', 1, 0, 'B', 2, 1, 'C', 3, 2])

    def test_uneven_groups(self):
        """Ensure ordered output from unevenly populated iterables"""
        eq_(list(roundrobin('ABCD', [1, 2], range(0))),
            ['A', 1, 'B', 2, 'C', 'D'])


class PowersetTests(TestCase):
    """Tests for ``powerset()``"""

    def test_combinatorics(self):
        """Ensure a proper enumeration"""
        p = powerset([1, 2, 3])
        eq_(list(p),
            [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)])


class UniqueEverseenTests(TestCase):
    """Tests for ``unique_everseen()``"""

    def test_everseen(self):
        """ensure duplicate elements are ignored"""
        u = unique_everseen('AAAABBBBCCDAABBB')
        eq_(['A', 'B', 'C', 'D'],
            list(u))

    def test_custom_key(self):
        """ensure the custom key comparison works"""
        u = unique_everseen('aAbACCc', key=str.lower)
        eq_(list('abC'), list(u))


class UniqueJustseenTests(TestCase):
    """Tests for ``unique_justseen()``"""

    def test_justseen(self):
        """ensure only last item is remembered"""
        u = unique_justseen('AAAABBBCCDABB')
        eq_(list('ABCDAB'), list(u))

    def test_custom_key(self):
        """ensure the custom key comparison works"""
        u = unique_justseen('AABCcAD', str.lower)
        eq_(list('ABCAD'), list(u))


class IterExceptTests(TestCase):
    """Tests for ``iter_except()``"""

    def test_exact_exception(self):
        """ensure the exact specified exception is caught"""
        l = [1, 2, 3]
        i = iter_except(l.pop, IndexError)
        eq_(list(i), [3, 2, 1])

    def test_generic_exception(self):
        """ensure the generic exception can be caught"""
        l = [1, 2]
        i = iter_except(l.pop, Exception)
        eq_(list(i), [2, 1])

    def test_uncaught_exception_is_raised(self):
        """ensure a non-specified exception is raised"""
        l = [1, 2, 3]
        i = iter_except(l.pop, KeyError)
        assert_raises(IndexError, list, i)

    def test_first(self):
        """ensure first is run before the function"""
        l = [1, 2, 3]
        f = lambda: 25
        i = iter_except(l.pop, IndexError, f)
        eq_(list(i), [25, 3, 2, 1])


class RandomProductTests(TestCase):
    """Tests for ``random_product()``

    Since random.choice() has different results with the same seed across
    python versions 2.x and 3.x, these tests use highly probably events to
    create predictable outcomes across platforms.
    """

    def test_simple_lists(self):
        """Ensure that one item is chosen from each list in each pair.
        Also ensure that each item from each list eventually appears in
        the chosen combinations.

        Odds are roughly 1 in 7.1 * 10e16 that one item from either list will
        not be chosen after 100 samplings of one item from each list. Just to
        be safe, better use a known random seed, too.

        """
        nums = [1, 2, 3]
        lets = ['a', 'b', 'c']
        n, m = zip(*[random_product(nums, lets) for _ in range(100)])
        n, m = set(n), set(m)
        eq_(n, set(nums))
        eq_(m, set(lets))
        eq_(len(n), len(nums))
        eq_(len(m), len(lets))

    def test_list_with_repeat(self):
        """ensure multiple items are chosen, and that they appear to be chosen
        from one list then the next, in proper order.

        """
        nums = [1, 2, 3]
        lets = ['a', 'b', 'c']
        r = list(random_product(nums, lets, repeat=100))
        eq_(2 * 100, len(r))
        n, m = set(r[::2]), set(r[1::2])
        eq_(n, set(nums))
        eq_(m, set(lets))
        eq_(len(n), len(nums))
        eq_(len(m), len(lets))


class RandomPermutationTests(TestCase):
    """Tests for ``random_permutation()``"""

    def test_full_permutation(self):
        """ensure every item from the iterable is returned in a new ordering

        15 elements have a 1 in 1.3 * 10e12 of appearing in sorted order, so
        we fix a seed value just to be sure.

        """
        i = range(15)
        r = random_permutation(i)
        eq_(set(i), set(r))
        if i == r:
            raise AssertionError("Values were not permuted")

    def test_partial_permutation(self):
        """ensure all returned items are from the iterable, that the returned
        permutation is of the desired length, and that all items eventually
        get returned.

        Sampling 100 permutations of length 5 from a set of 15 leaves a
        (2/3)^100 chance that an item will not be chosen. Multiplied by 15
        items, there is a 1 in 2.6e16 chance that at least 1 item will not
        show up in the resulting output. Using a random seed will fix that.

        """
        items = range(15)
        item_set = set(items)
        all_items = set()
        for _ in xrange(100):
            permutation = random_permutation(items, 5)
            eq_(len(permutation), 5)
            permutation_set = set(permutation)
            ok_(permutation_set <= item_set)
            all_items |= permutation_set
        eq_(all_items, item_set)


class RandomCombinationTests(TestCase):
    """Tests for ``random_combination()``"""

    def test_psuedorandomness(self):
        """ensure different subsets of the iterable get returned over many
        samplings of random combinations"""
        items = range(15)
        all_items = set()
        for _ in xrange(50):
            combination = random_combination(items, 5)
            all_items |= set(combination)
        eq_(all_items, set(items))

    def test_no_replacement(self):
        """ensure that elements are sampled without replacement"""
        items = range(15)
        for _ in xrange(50):
            combination = random_combination(items, len(items))
            eq_(len(combination), len(set(combination)))
        assert_raises(ValueError, random_combination, items, len(items) + 1)


class RandomCombinationWithReplacementTests(TestCase):
    """Tests for ``random_combination_with_replacement()``"""

    def test_replacement(self):
        """ensure that elements are sampled with replacement"""
        items = range(5)
        combo = random_combination_with_replacement(items, len(items) * 2)
        eq_(2 * len(items), len(combo))
        if len(set(combo)) == len(combo):
            raise AssertionError("Combination contained no duplicates")

    def test_psuedorandomness(self):
        """ensure different subsets of the iterable get returned over many
        samplings of random combinations"""
        items = range(15)
        all_items = set()
        for _ in xrange(50):
            combination = random_combination_with_replacement(items, 5)
            all_items |= set(combination)
        eq_(all_items, set(items))


class igetattrTests(TestCase):
    """Tests for ``igetattr()``"""

    class DummyObject(object):
        def __init__(self, value):
            self.foo = value

    def test_getattr(self):
        """Show that getattr() is getting applied to each element."""
        dummies = map(self.DummyObject, range(100))
        eq_(list(igetattr(dummies, 'foo')), range(100))

    def test_empty(self):
        """Show that the `default` keyword argument works."""
        dummies = map(self.DummyObject, range(100))
        eq_(list(igetattr(dummies, 'does_not_exist', 'defvalue')),
            list(repeat('defvalue', 100)))

