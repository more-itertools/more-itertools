===============
Version History
===============

.. automodule:: more_itertools

3.2.0
-----
* New itertools:
    * :func:`lstrip`, :func:`rstrip`, and :func:`strip`
      (thanks to MSeifert04 and pylang)
    * :func:`islice_extended`
* Improvements to existing itertools:
    * Some bugs with slicing :func:`peekable`-wrapped iterables were fixed

3.1.0
-----

* New itertools:
    * :func:`numeric_range` (Thanks to BebeSparkelSparkel and MSeifert04)
    * :func:`count_cycle` (Thanks to BebeSparkelSparkel)
    * :func:`locate` (Thanks to pylang and MSeifert04)
* Improvements to existing itertools:
    * A few itertools are now slightly faster due to some function
      optimizations. (Thanks to MSeifert04)
* The docs have been substantially revised with installation notes,
  categories for library functions, links, and more. (Thanks to pylang)


3.0.0
-----

* Removed itertools:
    * ``context`` has been removed due to a design flaw - see below for
      replacement options. (thanks to NeilGirdhar)
* Improvements to existing itertools:
    * ``side_effect`` now supports ``before`` and ``after`` keyword
      arguments. (Thanks to yardsale8)
* PyPy and PyPy3 are now supported.

The major version change is due to the removal of the ``context`` function.
Replace it with standard ``with`` statement context management:

.. code-block:: python

    # Don't use context() anymore
    file_obj = StringIO()
    consume(print(x, file=f) for f in context(file_obj) for x in u'123')

    # Use a with statement instead
    file_obj = StringIO()
    with file_obj as f:
        consume(print(x, file=f) for x in u'123')

2.6.0
-----

* New itertools:
    * ``adjacent`` and ``groupby_transform`` (Thanks to diazona)
    * ``always_iterable`` (Thanks to jaraco)
    * (Removed in 3.0.0) ``context`` (Thanks to yardsale8)
    * ``divide`` (Thanks to mozbhearsum)
* Improvements to existing itertools:
    * ``ilen`` is now slightly faster. (Thanks to wbolster)
    * ``peekable`` can now prepend items to an iterable. (Thanks to diazona)

2.5.0
-----

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
-----

* Move docs 100% to readthedocs.io.

2.4
-----

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
-----

* Added ``one`` from ``jaraco.util.itertools``. (Thanks, jaraco!)
* Added ``distinct_permutations`` and ``unique_to_each``. (Contributed by
  bbayles)
* Added ``windowed``. (Contributed by bbayles, with thanks to buchanae,
  jaraco, and abarnert)
* Simplified the implementation of ``chunked``. (Thanks, nvie!)
* Python 3.5 is now supported. Python 2.6 is no longer supported.
* Python 3 is now supported directly; there is no 2to3 step.

2.2
-----

* Added ``iterate`` and ``with_iter``. (Thanks, abarnert!)

2.1
-----

* Added (tested!) implementations of the recipes from the itertools
  documentation. (Thanks, Chris Lonnen!)
* Added ``ilen``. (Thanks for the inspiration, Matt Basta!)

2.0
-----

* ``chunked`` now returns lists rather than tuples. After all, they're
  homogeneous. This slightly backward-incompatible change is the reason for
  the major version bump.
* Added ``@consumer``.
* Improved test machinery.

1.1
-----

* Added ``first`` function.
* Added Python 3 support.
* Added a default arg to ``peekable.peek()``.
* Noted how to easily test whether a peekable iterator is exhausted.
* Rewrote documentation.

1.0
-----

* Initial release, with ``collate``, ``peekable``, and ``chunked``. Could
  really use better docs.
