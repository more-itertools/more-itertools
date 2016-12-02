"""Imported from the recipes section of the itertools documentation.

All functions taken from the recipes section of the itertools library docs
[1]_.
Some backward-compatible usability improvements have been made.

.. [1] http://docs.python.org/library/itertools.html#recipes

"""
from collections import deque
from itertools import (
    chain, combinations, count, cycle, groupby, islice, repeat, starmap, tee
)
import operator
from random import randrange, sample, choice

from six import PY2
from six.moves import filter, filterfalse, map, range, zip, zip_longest

__all__ = [
    'accumulate', 'all_equal', 'consume', 'dotproduct', 'first_true',
    'flatten', 'grouper', 'iter_except', 'ncycles', 'nth', 'padnone',
    'pairwise', 'partition', 'powerset', 'quantify',
    'random_combination_with_replacement', 'random_combination',
    'random_permutation', 'random_product', 'repeatfunc', 'roundrobin',
    'tabulate', 'tail', 'take', 'unique_everseen', 'unique_justseen'
]


def accumulate(iterable, func=operator.add):
    """
    Return an iterator whose items are the accumulated results of a function
    (specified by the optional *func* argument) that takes two arguments.
    By default, returns accumulated sums with ``operator.add()``.

        >>> list(accumulate([1, 2, 3, 4, 5]))  # Running sum
        [1, 3, 6, 10, 15]
        >>> list(accumulate([1, 2, 3], func=operator.mul))  # Running product
        [1, 2, 6]
        >>> list(accumulate([0, 1, -1, 2, 3, 2], func=max))  # Running maximum
        [0, 1, 1, 2, 3, 3]

    This function is available in the ``itertools`` module for Python 3.2 and
    greater.

    """
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    else:
        yield total

    for element in it:
        total = func(total, element)
        yield total


def take(n, iterable):
    """Return first n items of the iterable as a list

        >>> take(3, range(10))
        [0, 1, 2]
        >>> take(5, range(3))
        [0, 1, 2]

    Effectively a short replacement for ``next`` based iterator consumption
    when you want more than one item, but less than the whole iterator.

    """
    return list(islice(iterable, n))


def tabulate(function, start=0):
    """Return an iterator mapping the function over linear input.

    The start argument will be increased by 1 each time the iterator is called
    and fed into the function.

        >>> t = tabulate(lambda x: x**2, -3)
        >>> take(3, t)
        [9, 4, 1]

    """
    return map(function, count(start))


def tail(n, iterable):
    """
    Return an iterator over the last n items"

        >>> t = tail(3, 'ABCDEFG')
        >>> list(t)
        ['E', 'F', 'G']

    """
    return iter(deque(iterable, maxlen=n))


def consume(iterator, n=None):
    """Advance the iterator n-steps ahead. If n is none, consume entirely.

    Efficiently exhausts an iterator without returning values. Defaults to
    consuming the whole iterator, but an optional second argument may be
    provided to limit consumption.

        >>> i = (x for x in range(10))
        >>> next(i)
        0
        >>> consume(i, 3)
        >>> next(i)
        4
        >>> consume(i)
        >>> next(i)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration

    If the iterator has fewer items remaining than the provided limit, the
    whole iterator will be consumed.

        >>> i = (x for x in range(3))
        >>> consume(i, 5)
        >>> next(i)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration

    """
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    """Returns the nth item or a default value

        >>> l = range(10)
        >>> nth(l, 3)
        3
        >>> nth(l, 20, "zebra")
        'zebra'

    """
    return next(islice(iterable, n, None), default)


def all_equal(iterable):
    """
    Returns True if all the elements are equal to each other.

        >>> all_equal('aaaa')
        True
        >>> all_equal('aaab')
        False

    """
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def quantify(iterable, pred=bool):
    """Return the how many times the predicate is true

        >>> quantify([True, False, True])
        2

    """
    return sum(map(pred, iterable))


def padnone(iterable):
    """Returns the sequence of elements and then returns None indefinitely.

        >>> take(5, padnone(range(3)))
        [0, 1, 2, None, None]

    Useful for emulating the behavior of the built-in map() function.

    """
    return chain(iterable, repeat(None))


def ncycles(iterable, n):
    """Returns the sequence elements n times

        >>> list(ncycles(["a", "b"], 3))
        ['a', 'b', 'a', 'b', 'a', 'b']

    """
    return chain.from_iterable(repeat(tuple(iterable), n))


def dotproduct(vec1, vec2):
    """Returns the dot product of the two iterables

        >>> dotproduct([10, 10], [20, 20])
        400

    """
    return sum(map(operator.mul, vec1, vec2))


def flatten(listOfLists):
    """Return an iterator flattening one level of nesting in a list of lists

        >>> list(flatten([[0, 1], [2, 3]]))
        [0, 1, 2, 3]

    """
    return chain.from_iterable(listOfLists)


def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.

        >>> list(repeatfunc(lambda: 5, 3))
        [5, 5, 5]
        >>> list(repeatfunc(lambda x: x ** 2, 3, 3))
        [9, 9, 9]

    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))


def pairwise(iterable):
    """Returns an iterator of paired items, overlapping, from the original

        >>> take(4, pairwise(count()))
        [(0, 1), (1, 2), (2, 3), (3, 4)]

    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def grouper(n, iterable, fillvalue=None):
    """Collect data into fixed-length chunks or blocks

        >>> list(grouper(3, 'ABCDEFG', 'x'))
        [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]

    """
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def roundrobin(*iterables):
    """Yields an item from each iterable, alternating between them

        >>> list(roundrobin('ABC', 'D', 'EF'))
        ['A', 'D', 'E', 'B', 'F', 'C']

    """
    # Recipe credited to George Sakkis
    pending = len(iterables)
    if PY2:
        nexts = cycle(iter(it).next for it in iterables)
    else:
        nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


def partition(pred, iterable):
    """
    Returns a 2-tuple of iterables derived from the input iterable.
    The first yields the items that have ``pred(item) == False``.
    The first yields the items that have ``pred(item) == False``.

        >>> is_odd = lambda x: x % 2 != 0
        >>> iterable = range(10)
        >>> even_items, odd_items = partition(is_odd, iterable)
        >>> list(even_items), list(odd_items)
        ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])

    """
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


def powerset(iterable):
    """Yields all possible subsets of the iterable

        >>> list(powerset([1,2,3]))
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def unique_everseen(iterable, key=None):
    """
    Yield unique elements, preserving order.
        >>> list(unique_everseen('AAAABBBCCDAABBB'))
        ['A', 'B', 'C', 'D']
        >>> list(unique_everseen('ABBCcAD', str.lower))
        ['A', 'B', 'C', 'D']

    Sequences with a mix of hashable and unhashable items can be used.
    The function will be slower (i.e., O(N^2)) for unhashable items.

    """
    seenset = set()
    seenset_add = seenset.add
    seenlist = []
    seenlist_add = seenlist.append
    if key is None:
        for element in iterable:
            try:
                if element not in seenset:
                    seenset_add(element)
                    yield element
            except TypeError as e:
                if element not in seenlist:
                    seenlist_add(element)
                    yield element
    else:
        for element in iterable:
            k = key(element)
            try:
                if k not in seenset:
                    seenset_add(k)
                    yield element
            except TypeError as e:
                if k not in seenlist:
                    seenlist_add(k)
                    yield element


def unique_justseen(iterable, key=None):
    """Yields elements in order, ignoring serial duplicates

        >>> list(unique_justseen('AAAABBBCCDAABBB'))
        ['A', 'B', 'C', 'D', 'A', 'B']
        >>> list(unique_justseen('ABBCcAD', str.lower))
        ['A', 'B', 'C', 'A', 'D']

    """
    return map(next, map(operator.itemgetter(1), groupby(iterable, key)))


def iter_except(func, exception, first=None):
    """Yields results from a function repeatedly until an exception is raised.

    Converts a call-until-exception interface to an iterator interface.
    Like __builtin__.iter(func, sentinel) but uses an exception instead
    of a sentinel to end the loop.

        >>> l = [0, 1, 2]
        >>> list(iter_except(l.pop, IndexError))
        [2, 1, 0]

    """
    try:
        if first is not None:
            yield first()
        while 1:
            yield func()
    except exception:
        pass


def first_true(iterable, default=False, pred=None):
    """
    Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item for which
    ``pred(item) == True`` .

        >>> first_true(range(10))
        1
        >>> first_true(range(10), pred=lambda x: x > 5)
        6
        >>> first_true(range(10), default='missing', pred=lambda x: x > 9)
        'missing'

    """
    return next(filter(pred, iterable), default)


def random_product(*args, **kwds):
    """Returns a random pairing of items from each iterable argument

    If `repeat` is provided as a kwarg, it's value will be used to indicate
    how many pairings should be chosen.

        >>> random_product(['a', 'b', 'c'], [1, 2], repeat=2) # doctest:+SKIP
        ('b', '2', 'c', '2')

    """
    pools = [tuple(pool) for pool in args] * kwds.get('repeat', 1)
    return tuple(choice(pool) for pool in pools)


def random_permutation(iterable, r=None):
    """Returns a random permutation.

    If r is provided, the permutation is truncated to length r.

        >>> random_permutation(range(5)) # doctest:+SKIP
        (3, 4, 0, 1, 2)

    """
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(sample(pool, r))


def random_combination(iterable, r):
    """Returns a random combination of length r, chosen without replacement.

        >>> random_combination(range(5), 3) # doctest:+SKIP
        (2, 3, 4)

    """
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_combination_with_replacement(iterable, r):
    """Returns a random combination of length r, chosen with replacement.

        >>> random_combination_with_replacement(range(3), 5) # # doctest:+SKIP
        (0, 0, 1, 2, 2)

    """
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)
