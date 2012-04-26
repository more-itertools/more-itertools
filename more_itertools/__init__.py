from itertools import izip_longest


_marker = object()
def chunked(iterable, n):
    """Break an iterable into tuples of a given length.

    chunked([1, 2, 3, 4, 5, 6, 7], 3) --> [(1, 2, 3), (4, 5, 6), (7,)]

    If the length of ``iterable`` is not evenly divisible by ``n``, the last
    returned tuple will be shorter.

    """
    # Doesn't seem to run into any number-of-args limits.
    for group in izip_longest(*[iter(iterable)] * n, fillvalue=_marker):
        if group[-1] is _marker:
            # If this is the last group, shuck off the padding:
            group = tuple(x for x in group if x is not _marker)
        yield group


class peekable(object):
    """Wrapper for an iterator to allow 1-item lookahead
    
    Just call ``peek()`` on me to get the value that will next pop out of
    ``next()``.
    
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

    def peek(self):
        """Return the item that will be next returned from ``next()``.

        Raise ``StopIteration`` if there are no items left.

        """
        # TODO: Give peek a default arg. Raise StopIteration only when it isn't
        # provided. If it is, return the arg. Just like get('key', object())
        if not hasattr(self, '_peek'):
            self._peek = self._it.next()
        return self._peek

    def next(self):
        ret = self.peek()
        del self._peek
        return ret


def collate(*iterables, **kwargs):
    """Return an iterable ordered collation of the already-sorted items
    from each of ``iterables``, compared by kwarg ``key``.

    If ``reverse=True`` is passed, iterables must return their results in
    descending order rather than ascending.

    """
    key = kwargs.pop('key', lambda a: a)
    reverse = kwargs.pop('reverse', False)

    min_or_max = max if reverse else min
    peekables = [peekable(it) for it in iterables]
    peekables = [p for p in peekables if p]  # Kill empties.
    while peekables:
        _, p = min_or_max((key(p.peek()), p) for p in peekables)
        yield p.next()
        peekables = [p for p in peekables if p]
