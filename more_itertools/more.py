from __future__ import print_function

from collections import defaultdict, deque
from functools import partial, wraps
from heapq import merge
from itertools import chain, islice
from sys import version_info

from six import iteritems, string_types
from six.moves import filter, zip, zip_longest

from .recipes import take

__all__ = [
    'chunked', 'first', 'peekable', 'collate', 'consumer', 'ilen', 'iterate',
    'with_iter', 'one', 'distinct_permutations', 'intersperse',
    'unique_to_each', 'windowed', 'bucket', 'spy', 'interleave',
    'interleave_longest', 'collapse'
]


_marker = object()


def chunked(iterable, n):
    """Break an iterable into lists of a given length::

        >>> list(chunked([1, 2, 3, 4, 5, 6, 7], 3))
        [[1, 2, 3], [4, 5, 6], [7]]

    If the length of ``iterable`` is not evenly divisible by ``n``, the last
    returned list will be shorter.

    This is useful for splitting up a computation on a large number of keys
    into batches, to be pickled and sent off to worker processes. One example
    is operations on rows in MySQL, which does not implement server-side
    cursors properly and would otherwise load the entire dataset into RAM on
    the client.

    """
    iterable = iter(iterable)

    # To avoid leaving a reference to to the chunk in this generator function,
    # we put the chunk in a list and then pop it off the list when we yield.
    chunk_holder = []
    append = chunk_holder.append
    pop = chunk_holder.pop

    while True:
        append(list(islice(iterable, n)))
        if not chunk_holder[0]:
            return
        yield pop()


def first(iterable, default=_marker):
    """Return the first item of an iterable, ``default`` if there is none.

        >>> first([0, 1, 2, 3])
        0
        >>> first([], 'some default')
        'some default'

    If ``default`` is not provided and there are no items in the iterable,
    raise ``ValueError``.

    ``first()`` is useful when you have a generator of expensive-to-retrieve
    values and want any arbitrary one. It is marginally shorter than
    ``next(iter(...), default)``.

    """
    try:
        return next(iter(iterable))
    except StopIteration:
        # I'm on the edge about raising ValueError instead of StopIteration. At
        # the moment, ValueError wins, because the caller could conceivably
        # want to do something different with flow control when I raise the
        # exception, and it's weird to explicitly catch StopIteration.
        if default is _marker:
            raise ValueError('first() was called on an empty iterable, and no '
                             'default value was provided.')
        return default


class peekable(object):
    """Wrap an iterator to allow lookahead.

    Call ``peek()`` on the result to get the value that will next pop out of
    ``next()``, without advancing the iterator:

    >>> p = peekable(['a', 'b'])
    >>> p.peek()
    'a'
    >>> next(p)
    'a'

    Pass ``peek()`` a default value to return that instead of raising
    ``StopIteration`` when the iterator is exhausted.

    >>> p = peekable([])
    >>> p.peek('hi')
    'hi'

    You may index the peekable to look ahead by more than one item.
    The values up to the index you specified will be cached.
    Index 0 is the item that will be returned by ``next()``, index 1 is the
    item after that, and so on:

    >>> p = peekable(['a', 'b', 'c', 'd'])
    >>> p[0]
    'a'
    >>> p[1]
    'b'
    >>> next(p)
    'a'
    >>> p[1]
    'c'
    >>> next(p)
    'b'

    To test whether there are more items in the iterator, examine the
    peekable's truth value. If it is truthy, there are more items.

        >>> assert peekable([1])
        >>> assert not peekable([])

    """
    def __init__(self, iterable):
        self._it = iter(iterable)
        self._cache = deque()

    def __iter__(self):
        return self

    def __bool__(self):
        try:
            self.peek()
        except StopIteration:
            return False
        return True

    def __nonzero__(self):
        # For Python 2 compatibility
        return self.__bool__()

    def peek(self, default=_marker):
        """Return the item that will be next returned from ``next()``.

        Return ``default`` if there are no items left. If ``default`` is not
        provided, raise ``StopIteration``.

        """
        if not self._cache:
            try:
                self._cache.append(next(self._it))
            except StopIteration:
                if default is _marker:
                    raise
                return default
        return self._cache[0]

    def __next__(self):
        if self._cache:
            return self._cache.popleft()

        return next(self._it)

    def next(self):
        # For Python 2 compatibility
        return self.__next__()

    def _get_slice(self, index):
        start = index.start
        stop = index.stop

        if (
            ((start is not None) and (start < 0)) or
            ((stop is not None) and (stop < 0))
        ):
            raise ValueError('Negative indexing not supported')

        cache_len = len(self._cache)

        if stop is None:
            self._cache.extend(self._it)
        elif stop >= cache_len:
            self._cache.extend(islice(self._it, stop - cache_len))

        return list(self._cache)[index]

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._get_slice(index)

        return self._get_slice(slice(index, index + 1, None))[0]


def _collate(*iterables, **kwargs):
    """Helper for ``collate()``, called when the user is using the ``reverse``
    or ``key`` keyword arguments on Python versions below 3.5.

    """
    key = kwargs.pop('key', lambda a: a)
    reverse = kwargs.pop('reverse', False)

    min_or_max = partial(max if reverse else min, key=lambda a_b: a_b[0])
    peekables = [peekable(it) for it in iterables]
    peekables = [p for p in peekables if p]  # Kill empties.
    while peekables:
        _, p = min_or_max((key(p.peek()), p) for p in peekables)
        yield next(p)
        peekables = [x for x in peekables if x]


def collate(*iterables, **kwargs):
    """Return a sorted merge of the items from each of several already-sorted
    ``iterables``.

        >>> list(collate('ACDZ', 'AZ', 'JKL'))
        ['A', 'A', 'C', 'D', 'J', 'K', 'L', 'Z', 'Z']

    Works lazily, keeping only the next value from each iterable in memory. Use
    ``collate()`` to, for example, perform a n-way mergesort of items that
    don't fit in memory.

    :arg key: A function that returns a comparison value for an item. Defaults
        to the identity function.
    :arg reverse: If ``reverse=True``, yield results in descending order
        rather than ascending. ``iterables`` must also yield their elements in
        descending order.

    If the elements of the passed-in iterables are out of order, you might get
    unexpected results.

    If neither of the keyword arguments are specified, this function delegates
    to ``heapq.merge()``.

    """
    if not kwargs:
        return merge(*iterables)

    return _collate(*iterables, **kwargs)


# If using Python version 3.5 or greater, heapq.merge() will be faster than
# collate - use that instead.
if version_info >= (3, 5, 0):
    collate = merge


def consumer(func):
    """Decorator that automatically advances a PEP-342-style "reverse iterator"
    to its first yield point so you don't have to call ``next()`` on it
    manually.

    >>> @consumer
    ... def tally():
    ...     i = 0
    ...     while True:
    ...         print('Thing number %s is %s.' % (i, (yield)))
    ...         i += 1
    ...
    >>> t = tally()
    >>> t.send('red')
    Thing number 0 is red.
    >>> t.send('fish')
    Thing number 1 is fish.

    Without the decorator, you would have to call ``next(t)`` before
    ``t.send()`` could be used.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper


def ilen(iterable):
    """Return the number of items in ``iterable``.

    >>> ilen(x for x in range(1000000) if x % 3 == 0)
    333334

    This does, of course, consume the iterable, so handle it with care.

    """
    return sum(1 for _ in iterable)


def iterate(func, start):
    """Return ``start``, ``func(start)``, ``func(func(start))``, ...

    >>> from itertools import islice
    >>> list(islice(iterate(lambda x: 2*x, 1), 10))
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    """
    while True:
        yield start
        start = func(start)


def with_iter(context_manager):
    """Wrap an iterable in a ``with`` statement, so it closes once exhausted.

    For example, this will close the file when the iterator is exhausted::

        upper_lines = (line.upper() for line in with_iter(open('foo')))

    Any context manager which returns an iterable is a candidate for
    ``with_iter``.

    """
    with context_manager as iterable:
        for item in iterable:
            yield item


def one(iterable):
    """Return the only element from the iterable.

    Raise ValueError if the iterable is empty or longer than 1 element. For
    example, assert that a DB query returns a single, unique result.

    >>> one(['val'])
    'val'

    >>> one(['val', 'other'])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ValueError: too many values to unpack (expected 1)

    >>> one([])
    Traceback (most recent call last):
    ...
    ValueError: need more than 0 values to unpack

    ``one()`` attempts to advance the iterable twice in order to ensure there
    aren't further items. Because this discards any second item, ``one()`` is
    not suitable in situations where you want to catch its exception and then
    try an alternative treatment of the iterable. It should be used only when a
    iterable longer than 1 item is, in fact, an error.

    """
    it = iter(iterable)
    first = next(it, _marker)
    if first is _marker:
        raise ValueError('need more than 0 values to unpack')

    second = next(it, _marker)
    if second is not _marker:
        raise ValueError('too many values to unpack (expected 1)')

    return first


def distinct_permutations(iterable):
    """Yield successive distinct permutations of the elements in the iterable.

    Equivalent to ``set(permutations(iterable))``, except duplicates are not
    generated. For large input sequences, this is much more efficient.

    """
    def perm_unique_helper(item_counts, perm, i):
        """Internal helper function

        :arg item_counts: Stores the unique items in ``iterable`` and how many
            times they are repeated
        :arg perm: The permutation that is being built for output
        :arg i: The index of the permutation being modified

        The output permutations are built up recursively; the distinct items
        are placed until their repetitions are exhausted.
        """
        if i < 0:
            yield tuple(perm)
        else:
            for item in item_counts:
                if item_counts[item] <= 0:
                    continue
                perm[i] = item
                item_counts[item] -= 1
                for x in perm_unique_helper(item_counts, perm, i - 1):
                    yield x
                item_counts[item] += 1

    item_counts = {}
    for item in iterable:
        item_counts[item] = item_counts.get(item, 0) + 1

    return perm_unique_helper(item_counts, [None] * len(iterable),
                              len(iterable) - 1)


def intersperse(e, iterable):
    """Intersperse element ``e`` between the elements of an iterable.

    >>> from more_itertools import intersperse
    >>> list(intersperse('x', [1, 'o', 5, 'k']))
    [1, 'x', 'o', 'x', 5, 'x', 'k']
    >>> list(intersperse(None, [1, 2, 3]))
    [1, None, 2, None, 3]
    >>> list(intersperse('x', 1))
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable
    >>> list(intersperse('x', []))
    []

    """
    iterable = iter(iterable)
    if iterable:
        yield next(iterable)
        for item in iterable:
            yield e
            yield item
    raise StopIteration


def unique_to_each(*iterables):
    """Return the elements from each of the input iterables that aren't in the
    other input iterables.

    For example, suppose packages 1, 2, and 3 have these dependencies:
    pkg_1: (A, B), pkg_2: (B, C), pkg_3: (B, D)

    If you remove one package, which dependencies can also be removed?

    If pkg_1 is removed, then A is no longer necessary - it is not associated
    with pkg_2 or pkg_3. Similarly, C is only needed for pkg_2, and D is
    only needed for pkg_3:
    >>> unique_to_each("AB", "BC", "BD")
    [['A'], ['C'], ['D']]

    If there are duplicates in one input iterable that aren't in the others
    they will be duplicated in the output. Input order is preserved:
    >>> unique_to_each("mississippi", "missouri")
    [['p', 'p'], ['o', 'u', 'r']]

    It is assumed that the elements of each iterable are hashable.

    """
    elements_to_indices = {}
    pool = [list(it) for it in iterables]
    for i, it in enumerate(pool):
        for element in it:
            elements_to_indices.setdefault(element, set()).add(i)

    for element, indices in iteritems(elements_to_indices):
        if len(indices) != 1:
            for i in indices:
                while element in pool[i]:
                    pool[i].remove(element)

    return pool


def windowed(seq, n, fillvalue=None):
    """Return a sliding window (of width n) over data from the iterable.

    When n=2 this is equivalent to ``pairwise(iterable)``.
    When n is larger than the iterable, ``fillvalue`` is used in place of
    missing values.

    >>> all_windows = windowed([1, 2, 3, 4, 5], 3)
    >>> next(all_windows)
    (1, 2, 3)
    >>> next(all_windows)
    (2, 3, 4)
    >>> next(all_windows)
    (3, 4, 5)

    """
    if n < 0:
        raise ValueError('n must be >= 0')
    if n == 0:
        yield tuple()
        return

    it = iter(seq)
    window = deque([], n)
    append = window.append

    # Initial deque fill
    for _ in range(n):
        append(next(it, fillvalue))
    yield tuple(window)

    # Appending new items to the right causes old items to fall off the left
    for item in it:
        append(item)
        yield tuple(window)


class bucket(object):
    """Wrap an iterable and return an object that buckets the iterable into
    child iterables based on a ``key`` function.

    >>> iterable = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'b3']
    >>> s = bucket(iterable, key=lambda s: s[0])  # Select by first character
    >>> a_iterable = s['a']
    >>> next(a_iterable)
    'a1'
    >>> next(a_iterable)
    'a2'
    >>> list(s['b'])
    ['b1', 'b2', 'b3']

    The original iterable will be advanced and its items will be cached until
    they are used by the child iterables. This may require significant storage.
    Be aware that attempting to select a bucket that no items correspond to
    will exhaust the iterable and cache all values.

    """
    def __init__(self, iterable, key):
        self._it = iter(iterable)
        self._key = key
        self._cache = defaultdict(deque)

    def __contains__(self, value):
        try:
            item = next(self[value])
        except StopIteration:
            return False
        else:
            self._cache[value].appendleft(item)

        return True

    def _get_values(self, value):
        """
        Helper to yield items from the parent iterator that match *value*.
        Items that don't match are stored in the local cache as they
        are encountered.
        """
        while True:
            # If we've cached some items that match the target value, emit
            # the first one and evict it from the cache.
            if self._cache[value]:
                yield self._cache[value].popleft()
            # Otherwise we need to advance the parent iterator to search for
            # a matching item, caching the rest.
            else:
                while True:
                    item = next(self._it)
                    item_value = self._key(item)
                    if item_value == value:
                        yield item
                        break
                    else:
                        self._cache[item_value].append(item)

    def __getitem__(self, value):
        return self._get_values(value)


def spy(iterable, n=1):
    """Return a 2-tuple with a list containing the first *n* elements of
    *iterable*, and an iterator with the same items as *iterable*.
    This allows you to "look ahead" at the items in the iterable without
    advancing it.

    There is one item in the list by default:

        >>> iterable = 'abcdefg'
        >>> head, iterable = spy(iterable)
        >>> head
        ['a']
        >>> list(iterable)
        ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    You may use unpacking to retrieve items instead of lists:

        >>> (head,), iterable = spy('abcdefg')
        >>> head
        'a'
        >>> (first, second), iterable = spy('abcdefg', 2)
        >>> first
        'a'
        >>> second
        'b'

    The number of items requested can be larger than the number of items in
    the iterable:

        >>> iterable = [1, 2, 3, 4, 5]
        >>> head, iterable = spy(iterable, 10)
        >>> head
        [1, 2, 3, 4, 5]
        >>> list(iterable)
        [1, 2, 3, 4, 5]

    """
    it = iter(iterable)
    head = take(n, it)

    return head, chain(head, it)


def interleave(*iterables):
    """Return a new iterable yielding from each iterable in turn,
    until the shortest is exhausted. Note that this is the same as
    chain(*zip(*iterables)).

    >>> list(interleave([1, 2, 3], [4, 5], [6, 7, 8]))
    [1, 4, 6, 2, 5, 7]
    """
    return chain.from_iterable(zip(*iterables))


def interleave_longest(*iterables):
    """Return a new iterable yielding from each iterable in turn,
    skipping any that are exhausted. Note that this is not the same as
    chain(*zip_longest(*iterables)).

    >>> list(interleave_longest([1, 2, 3], [4, 5], [6, 7, 8]))
    [1, 4, 6, 2, 5, 7, 3, 8]
    """
    i = chain.from_iterable(zip_longest(*iterables, fillvalue=_marker))
    return filter(lambda x: x is not _marker, i)


def collapse(iterable, base_type=None, levels=None):
    """Flatten an iterable containing some iterables (themselves containing
    some iterables, etc.) into non-iterable types, strings, elements
    matching ``isinstance(element, base_type)``, and elements that are
    ``levels`` levels down.

    >>> list(collapse([[1], 2, [[3], 4], [[[5]]], 'abc']))
    [1, 2, 3, 4, 5, 'abc']
    >>> list(collapse([[1], 2, [[3], 4], [[[5]]]], levels=2))
    [1, 2, 3, 4, [5]]
    >>> list(collapse((1, [2], (3, [4, (5,)])), list))
    [1, [2], 3, [4, (5,)]]
    """
    def walk(node, level):
        if (
            ((levels is not None) and (level > levels)) or
            isinstance(node, string_types) or
            ((base_type is not None) and isinstance(node, base_type))
        ):
            yield node
            return

        try:
            tree = iter(node)
        except TypeError:
            yield node
            return
        else:
            for child in tree:
                for x in walk(child, level + 1):
                    yield x

    for x in walk(iterable, 0):
        yield x
