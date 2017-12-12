from __future__ import print_function


def seekable_example():
    """If you've worked with iterators in Python, you have probably found yourself
    wondering whether you could "reset" them, i.e. revisit previous items.

        >>> it = (str(n) for n in range(5))
        >>> list(it)
        ['0', '1', '2', '3', '4']

    Alas, iterators are unidirectional. Once they're exhausted, they can't be
    revived:

        >>> list(it)
        []

    If you want to keep old values, you have to cache them yourself.

        >>> it = (str(n) for n in range(5))
        >>> cache = []
        >>> for item in it:
        ...    cache.append(item)

    Then you can review the items:

        >>> review_it = iter(cache)
        >>> next(review_it)
        '0'

    :class:`seekable` automates this process. It caches the iterable's items
    as you go and then lets you "rewind" to a specified index in the cache
    with the :meth:`seek` method.

        >>> from more_itertools import seekable
        >>> it = seekable(str(n) for n in range(5))
        >>> list(it)
        ['0', '1', '2', '3', '4']
        >>> it.seek(0)
        >>> list(it)
        ['0', '1', '2', '3', '4']



    """
