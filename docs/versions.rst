===============
Version History
===============

2.6.0
    * New itertools:
        * ``adjacent`` and ``groupby_transform`` (Thanks to diazona)
        * ``always_iterable`` (Thanks to jaraco)
        * ``context`` (Thanks to yardsale8)
        * ``divide`` (Thanks to mozbhearsum)
    * Improvements to existing itertools:
        * ``ilen`` is now slightly faster. (Thanks to wbolster)
        * ``peekable`` can now prepend items to an iterable. (Thanks to diazona)

2.5.0
    * New itertools:
        * ``distribute`` (Thanks to mozbhearsum and coady)
        * ``sort_together`` (Thanks to clintval)
        * ``stagger`` and ``zip_offset`` (Thanks to joshbode)
        * ``padded``
    * Improvements to existing itertools:
        * ``peekable`` now handles negative indexes and slices with negative
          components properly.
        * ``intersperse`` is now slightly faster. (Thanks to pylang)
        * ``windowed`` now accepts a ``step`` keyword argument.
          (Thanks to pylang)
    * Python 3.6 is now supported.

2.4.1
    * Move docs 100% to readthedocs.io.

2.4
    * New itertools:
        * ``accumulate``, ``all_equal``, ``first_true``, ``partition``, and
          ``tail`` from the itertools documentation.
        * ``bucket`` (Thanks to Rosuav and cvrebert)
        * ``collapse`` (Thanks to abarnet)
        * ``interleave`` and ``interleave_longest`` (Thanks to abarnet)
        * ``side_effect`` (Thanks to nvie)
        * ``sliced`` (Thanks to j4mie and coady)
        * ``split_before`` and ``split_after`` (Thanks to astronouth7303)
        * ``spy`` (Thanks to themiurgo and mathieulongtin)
    * Improvements to existing itertools:
        * ``chunked`` is now simpler and more friendly to garbage collection.
          (Contributed by coady, with thanks to piskvorky)
        * ``collate`` now delegates to ``heapq.merge`` when possible.
          (Thanks to kmike and julianpistorius)
        * ``peekable``-wrapped iterables are now indexable and sliceable.
          Iterating through ``peekable``-wrapped iterables is also faster.
        * ``one`` and ``unique_to_each`` have been simplified.
          (Thanks to coady)


2.3
    * Added ``one`` from ``jaraco.util.itertools``. (Thanks, jaraco!)
    * Added ``distinct_permutations`` and ``unique_to_each``. (Contributed by
      bbayles)
    * Added ``windowed``. (Contributed by bbayles, with thanks to buchanae,
      jaraco, and abarnert)
    * Simplified the implementation of ``chunked``. (Thanks, nvie!)
    * Python 3.5 is now supported. Python 2.6 is no longer supported.
    * Python 3 is now supported directly; there is no 2to3 step.

2.2
    * Added ``iterate`` and ``with_iter``. (Thanks, abarnert!)

2.1
    * Added (tested!) implementations of the recipes from the itertools
      documentation. (Thanks, Chris Lonnen!)
    * Added ``ilen``. (Thanks for the inspiration, Matt Basta!)

2.0
    * ``chunked`` now returns lists rather than tuples. After all, they're
      homogeneous. This slightly backward-incompatible change is the reason for
      the major version bump.
    * Added ``@consumer``.
    * Improved test machinery.

1.1
    * Added ``first`` function.
    * Added Python 3 support.
    * Added a default arg to ``peekable.peek()``.
    * Noted how to easily test whether a peekable iterator is exhausted.
    * Rewrote documentation.

1.0
    * Initial release, with ``collate``, ``peekable``, and ``chunked``. Could
      really use better docs.
