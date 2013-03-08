from functools import partial, wraps
from itertools import izip_longest
from recipes import *

__all__ = ['chunked', 'first', 'peekable', 'collate', 'consumer', 'ilen',
           'iterate', 'with_iter']


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
    # Doesn't seem to run into any number-of-args limits.
    for group in (list(g) for g in izip_longest(*[iter(iterable)] * n,
                                                fillvalue=_marker)):
        if group[-1] is _marker:
            # If this is the last group, shuck off the padding:
            del group[group.index(_marker):]
        yield group


def first(iterable, default=_marker):
    """Return the first item of an iterable, ``default`` if there is none.

        >>> first(xrange(4))
        0
        >>> first(xrange(0), 'some default')
        'some default'

    If ``default`` is not provided and there are no items in the iterable,
    raise ``ValueError``.

    ``first()`` is useful when you have a generator of expensive-to-retrieve
    values and want any arbitrary one. It is marginally shorter than
    ``next(iter(...))`` but saves you an entire ``try``/``except`` when you
    want to provide a fallback value.

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
    """Wrapper for an iterator to allow 1-item lookahead

    Call ``peek()`` on the result to get the value that will next pop out of
    ``next()``, without advancing the iterator:

        >>> p = peekable(xrange(2))
        >>> p.peek()
        0
        >>> p.next()
        0
        >>> p.peek()
        1
        >>> p.next()
        1

    Pass ``peek()`` a default value, and it will be returned in the case where
    the iterator is exhausted:

        >>> p = peekable([])
        >>> p.peek('hi')
        'hi'

    If no default is provided, ``peek()`` raises ``StopIteration`` when there
    are no items left.

    To test whether there are more items in the iterator, examine the
    peekable's truth value. If it is truthy, there are more items.

        >>> assert peekable(xrange(1))
        >>> assert not peekable([])

    """
    # Lowercase to blend in with itertools. The fact that it's a class is an
    # implementation detail.

    def __init__(self, iterable):
        self._it = iter(iterable)

    def __iter__(self):
        return self

    def __nonzero__(self):
        try:
            self.peek()
        except StopIteration:
            return False
        return True

    def peek(self, default=_marker):
        """Return the item that will be next returned from ``next()``.

        Return ``default`` if there are no items left. If ``default`` is not
        provided, raise ``StopIteration``.

        """
        if not hasattr(self, '_peek'):
            try:
                self._peek = self._it.next()
            except StopIteration:
                if default is _marker:
                    raise
                return default
        return self._peek

    def next(self):
        ret = self.peek()
        del self._peek
        return ret


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

    """
    key = kwargs.pop('key', lambda a: a)
    reverse = kwargs.pop('reverse', False)

    min_or_max = partial(max if reverse else min, key=lambda (a, b): a)
    peekables = [peekable(it) for it in iterables]
    peekables = [p for p in peekables if p]  # Kill empties.
    while peekables:
        _, p = min_or_max((key(p.peek()), p) for p in peekables)
        yield p.next()
        peekables = [p for p in peekables if p]


def consumer(func):
    """Decorator that automatically advances a PEP-342-style "reverse iterator"
    to its first yield point so you don't have to call ``next()`` on it
    manually.

    >>> @consumer
    ... def tally():
    ...     i = 0
    ...     while True:
    ...         print 'Thing number %s is %s.' % (i, (yield))
    ...         i += 1
    ...
    >>> t = tally()
    >>> t.send('red')
    Thing number 0 is red.
    >>> t.send('fish')
    Thing number 1 is fish.

    Without the decorator, you would have to call ``t.next()`` before
    ``t.send()`` could be used.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.next()
        return gen
    return wrapper


def ilen(iterable):
    """Return the number of items in ``iterable``.

    >>> from itertools import ifilter
    >>> ilen(ifilter(lambda x: x % 3 == 0, xrange(1000000)))
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

    Example::

        upper_lines = (line.upper() for line in with_iter(open('foo')))

    """
    with context_manager as iterable:
        for item in iterable:
            yield item
