===============
Version History
===============

.. automodule:: more_itertools
   :noindex:

10.8.0
------

* New functions:
    * :func:`derangements` was added (thanks to debruijn)
    * :func:`argmin` and :func:`argmax` were added (thanks to rhettinger)
    * :func:`running_median` was added (thanks to rhettinger)
    * :func:`extract` was added (thanks to rhettinger)
    * :func:`interleave_randomly` was added (thanks to ktbarrett)

* Changes to existing functions:
    * The type hints and docstring for :func:`batched` were improved (thanks to qobilidop and inventshah)
    * The memory usage of :func:`islice_extended` was reduced (thanks to ben42code)
    * The performance of :func:`sample` and :func:`consecutive_groups`, :func:`dft`, :func:`idft`, :func:`map_if`, :func:`count_cycle`, and :func:`tail` were improved (thanks to rhettinger) 
    * The performance of :func:`before_and_after`, :func:`mark_ends`, and :func:`interleave_longest` were improved (thanks to pochmann3) 
    * :func:`nth_prime` now accepts an ``approximate`` keyword. When set to ``True``, a faster but less accurate method is used to return a result. (thanks to rhettinger)
    * :func:`last` now works when its input has ``__reversed__`` set to ``None`` (thanks to inventshah)
    * The :func:`unzip` function was simplified (thanks to pochmann3)
    * The :func:`reshape` function now accepts ``shape`` values that represent multidimensional matrices (thanks to rhettinger)

* Other changes:
    * An issue with dark themes and documentation display was fixed (thanks to pochmann3, moreati, and pradyunsg)
    * Variable names in several functions were improved (thanks to rhettinger)
    * The docstrings for :func:`dft`, :func:`idft`, :func:`minmax`, :func:`sample`, and :func:`multinomial` were improved (thanks to rhettinger)
    * Packaging and package index metadata were improved (thanks to cdce8p)
    * Several aspects of the documentation were improved (thanks to rhettinger, saadmanrafat)
    * The Makefile now refers to `python` instead of `python3` (thanks to ktbarrett)
    * Test coverage was improved (thanks to rhettinger)
    * Python 3.14 is now tested by GitHub Actions

10.7.0
------

* New functions:
    * :func:`multinomial` was added (thanks to rhettinger)

* Changes to existing functions:
    * :func:`ichunked`, :func:`iterate`, :func:`one`, :func:`only`, :func:`powerset_of_sets`, and :func:`strictly_n` were optimized (thanks to rhettinger)
    * :func:`exactly_n` now uses less memory (thanks to rhettinger)
    * :func:`dft` and :func:`idft` were optimized for Python versions below 3.12 (thanks to rhettinger)
    * :func:`is_prime` no longer shares state with the users random number generator (thanks to rhettinger)

* Other changes:
    * Some docstring issues were fixed (thanks to lpulley and ricbit)
    * The type hints for :func:`groupby_transform` were improved (thanks to rhettinger)
    * The ``furo`` theme is now used for docs (thanks to AA-turner)


10.6.0
------

* New functions:
    * :func:`is_prime` and :func:`nth_prime` were added (thanks to JamesParrott and rhettinger)
    * :func:`loops` was added (thanks to rhettinger)

* Changes to existing functions:
    * :func:`factor` was optimized to handle larger inputs and use less memory (thanks to rhettinger)
    * :func:`spy` was optimized to enable nested calls (thanks to rhettinger)
    * :func:`polynomial_from_roots` was made non-recursive and able to handle larger numbers of roots (thanks to pochmann3 and rhettinger)
    * :func:`is_sorted` now only relies on less than comparisons (thanks to rhettinger)
    * The docstring for :func:`outer_product` was improved (thanks to rhettinger)
    * The type annotations for :func:`sample` were improved (thanks to rhettinger)

* Other changes:
    * Python 3.13 is officially supported. Python 3.8 is no longer officially supported. (thanks to hugovk, JamesParrott, and stankudrow)
    * `mypy` checks were fixed (thanks to JamesParrott)

10.5.0
------

* Bug fixes
    * A missing symbol in ``more.pyi`` was fixed (thanks to eberts-google and nathanielmanistaatgoogle)

* Other changes
    * :func:`all_equal` was optimized (thanks to pochmann3 and rhettinger)

10.4.0
------

* Changes to existing functions
    * :func:`circular_shifts` now accepts a ``steps`` parameter (thanks to rhettinger)
    * :func:`distinct_permutations` now accepts iterables with non-comparable items (thanks to hgustafsson, JamesParrott, and pochmann3)
    * :class:`run_length`, :func:`totient`, :func:`sliding_window`, and :func:`triplewise` were optimized (thanks to rhettinger)
    * :class:`ilen` was optimized (thanks to pochmann3 and rhettinger)
    * :func:`sample` was improved, and now accepts ``counts`` and ``strict`` parameters (thanks to rhettinger)
    * :func:`set_partitions` now accepts ``min_size`` and ``max_size`` parameters (thanks to Pandede)
    * :func:`seekable`'s ``relative_seek`` method remembers previous calls (thanks to dkrikun)
    * :func:`sort_together` now accepts a ``strict`` parameter (thanks to rhettinger and Pandede)

* Other changes
    * The docs for :func:`is_sorted` and :func:`strictly_n` were improved (thanks to pochmann3 and fakuivan)
    * The typing information for :func:`windowed_complete`, :func:`zip_broadcast`, and :func:`zip_equal` were improved (thanks to m472, eyalho, akisatoon1, jbosboom, and Pandede)

10.3.0
------

* New functions
    * :func:`powerset_of_sets`, :func:`dft`, and :func:`idft` (thanks to rhettinger)
    * :func:`join_mappings` (thanks to NeilGirdhar and rhettinger)
    * :func:`doublestarmap` (thanks to Skeen, monk-time, DamianB-BitFlipper, and ergoithz)
    * :func:`unique` (thanks to rhettinger)

* Changes to existing functions
    * :func:`collapse`, :func:`chunked_even`, :func:`ichunked`, :func:`padded`, and :func:`windowed` were optimized and improved (thanks to james-wasson)
    * :func:`totient` was optimized (thanks to rhettinger)
    * :func:`roundrobin` was updated and improved (thanks to rhettinger)
    * :func:`all_equal` now accepts a *key* parameter.
    * The docs for :func:`value_chain` were improved (thanks to bjrtx)
    * The type annotations for :class:`countable` were improved (thanks to aidanholm)

* Other changes
    * Unit tests were improved (thanks to haukex)
    * Some documentation issues were fixed (thanks to bjrtx and DimitriPapadopoulos)

10.2.0
------

* New functions
    * :func:`iter_suppress` (thanks to jaraco, pochmann, and rhettinger)
    * :func:`filter_map` (thanks to struktured)
    * :func:`classify_unique` (thanks to haukex)
    * :func:`totient` (from the itertools docs)
    * :func:`reshape` (from the itertools docs)

* Changes to existing functions
    * :func:`factor`, :func:`iter_index`, :func:`sieve`, and :func:`unique_justseen` were updated to match the itertools docs
    * :func:`first` was optimized (thanks to pochmann)
    * :func:`takewhile_inclusive` was refactored (thanks to eltoder)
    * :func:`combination_with_replacement_index` was optimized (thanks to elliotwutingfeng and rhettinger)
    * :func:`nth_permutation`, :func:`nth_combination_with_replacement`, :func:`combination_index`, and :func:`combination_with_replacement_index` were optimized (thanks to rhettinger)
    * :func:`batched` now accepts a `strict` argument (adapted from itertools docs)
    * :func:`time_limited` was improved for Windows (thanks to haukex)

* Other changes
    * Several typing updates were made (thanks to obaltian and ilai-deutel)
    * Some documentation issues were fixed (thanks to F-park, DimitriPapadopoulos, peterbygrave, shuuji3, eltoder, and homeworkprod)

10.1.0
------

* New functions
    * :func:`takewhile_inclusive` (thanks to OlegAlexander)
    * :func:`outer_product` (thanks to OlegAlexander)

* Changes to existing functions
    * :func:`zip_broadcast` was improved (thanks to kalekundert and pochmann)
    * :func:`consume` had its type annotation fixed (thanks to obaltian)

* Other changes
    * Some documentation and testing issues were fixed (thanks to OlegAlexander)

10.0.0
------

* Potentially breaking changes
    * Python 3.7 support was dropped, since it went EOL on 2023-06-27
    * :func:`batched` no longer issues a ``DeprecationWarning``; it is now an alias for ``itertools.batched`` for Python 3.12+
    * :func:`batched` and :func:`matmul` now yield tuples instead of lists

* New functions
    * :func:`combination_with_replacement_index` (thanks to Schoyen)
    * :func:`nth_combination_with_replacement` (thanks to Schoyen)
    * :func:`polynomial_eval` (from the Python itertools docs)
    * :func:`polynomial_derivative` (from the Python itertools docs)
    * :func:`sum_of_squares` (from the Python itertools docs)

* Changes to existing functions
    * :func:`seekable` now has ``relative_seek`` method (thanks to karlb)
    * :func:`chunked_even` was optimized (thanks to elliotwutingfeng)
    * :func:`numeric_range` was optimized (thanks to eltoder)
    * :func:`duplicates_justseen`, :func:`pairwise`, :func:`partial_product`, and :func:`partition` were updated and optimized (thanks to pochmann)
    * :func:`unique_in_window` had its implementation updated (thanks to elliotwutingfeng)
    * :func:`iterate` now breaks when its ``func`` argument raises ``StopIteration`` (thanks to jrebiffe)

* Other changes
    * Some documentation and testing issues were fixed (thanks to lonnen and XuehaiPan)

9.1.0
-----

* New functions
    * :func:`iter_index` (from the Python itertools docs)
    * :func:`transpose` (from the Python itertools docs)
    * :func:`matmul` (from the Python itertools docs)
    * :func:`factor` (from the Python itertools docs)
    * :func:`gray_product` (thanks to haukex)
    * :func:`partial_product` (thanks to lonnen)

* Changes to existing functions
    * :func:`sieve` was updated to match the Python itertools docs
    * :func:`maxsplit` was updated to fix a bug (thanks to abingham)
    * :func:`sliced` had its `type hint <https://github.com/more-itertools/more-itertools/pull/667>`__ updated (thanks to ad-chaos)


* Other changes
    * The ``batched`` function is marked as deprecated and will be removed in a future major release. For Python 3.12 and above, use ``itertools.batched`` instead. (thanks to neutrinoceros)
    * The type hints now used postponed evaluation of annotations from PEP 563 (thanks to Isira-Seneviratne)
    * Some documentation issues were fixed (thanks to Voskov and jdkandersson)

9.0.0
-----

* Potentially breaking changes
    * :func:`grouper` no longer accepts an integer as its first argument. Previously this raised a ``DeprecationWarning``.
    * :func:`collate` has been removed. Use the built-in :func:`heapq.merge` instead.
    * :func:`windowed` now yields nothing when its iterable is empty.
    * This library now advertises support for Python 3.7+.

* New functions
    * :func:`constrained_batches`
    * :func:`batched` (from the Python itertools docs)
    * :func:`polynomial_from_roots` (from the Python itertools docs)
    * :func:`sieve` (from the Python itertools docs)

* Other changes
    * Some documentation issues were fixed (thanks to nanouasyn)

8.14.0
------

* New functions
    * :func:`longest_common_prefix` (thanks to nanouasyn)
    * :func:`iequals` (thanks to nanouasyn)

* Changes to existing functions
    * `concurrent.futures.ThreadPoolExecutor` is now imported lazily in :func:`callback_iter`.
    * :func:`tail` is now optimized for iterables with a fixed length.

* Other changes
    * Some documentation issues were fixed (thanks to pochmann and timgates42)
    * This library is now marked for Python 3.10 compatibility in PyPI (thanks to chayim)

8.13.0
------

* New functions
    * The :func:`subslices` recipe from the `itertools` docs was added (thanks to rhettinger)

* Changes to existing functions
    * The :func:`ichunked` function is now more efficient (thanks to hjtran0 and seanmacavaney)
    * The :func:`difference` function is now more efficient (thanks to Masynchin)
    * The :func:`grouper` recipe now has more features, mirroring the one in the `itertools` docs (thanks to rhettinger)

* Other changes
    * Some documentation issues were fixed (thanks to medvied and Freed-Wu)
    * The `more_itertools` package is now built with `flit` (thanks to mgorny)

8.12.0
------

* Bug fixes
    * Some documentation issues were fixed (thanks to Masynchin, spookylukey, astrojuanlu, and stephengmatthews)
    * Python 3.5 support was temporarily restored (thanks to mattbonnell)

8.11.0
------

* New functions
    * The :func:`before_and_after`, :func:`sliding_window`, and :func:`triplewise` recipes from the Python 3.10 docs were added
    * :func:`duplicates_everseen` and :func:`duplicates_justseen` (thanks to OrBin and DavidPratt512)
    * :func:`minmax` (thanks to Ricocotam, MSeifert04, and ruancomelli)
    * :func:`strictly_n` (thanks to hwalinga and NotWearingPants)
    * :func:`unique_in_window`

* Changes to existing functions
    * :func:`groupby_transform` had its type stub improved (thanks to mjk4 and ruancomelli)
    * :func:`is_sorted` now accepts a ``strict`` parameter (thanks to Dutcho and ruancomelli)
    * :func:`zip_broadcast` was updated to fix a bug (thanks to kalekundert)

8.10.0
------

* Changes to existing functions
    * The type stub for :func:`iter_except` was improved (thanks to  MarcinKonowalczyk)

* Other changes:
    *  Type stubs now ship with the source release (thanks to saaketp)
    *  The Sphinx docs were improved (thanks to MarcinKonowalczyk)

8.9.0
-----

* New functions
    * :func:`interleave_evenly` (thanks to mbugert)
    * :func:`repeat_each` (thanks to FinalSh4re)
    * :func:`chunked_even` (thanks to valtron)
    * :func:`map_if` (thanks to sassbalint)
    * :func:`zip_broadcast` (thanks to kalekundert)

* Changes to existing functions
    * The type stub for :func:`chunked` was improved (thanks to  PhilMacKay)
    * The type stubs for :func:`zip_equal` and `zip_offset` were improved (thanks to maffoo)
    * Building Sphinx docs locally was improved (thanks to MarcinKonowalczyk)

8.8.0
-----

* New functions
    * :func:`countable` (thanks to krzysieq)

* Changes to existing functions
    * :func:`split_before` was updated to handle empty collections (thanks to TiunovNN)
    * :func:`unique_everseen` got a performance boost (thanks to Numerlor)
    * The type hint for :func:`value_chain` was corrected (thanks to vr2262)

8.7.0
-----

* New functions
    * :func:`convolve` (from the Python itertools docs)
    * :func:`product_index`, :func:`combination_index`, and :func:`permutation_index` (thanks to N8Brooks)
    * :func:`value_chain` (thanks to jenstroeger)

* Changes to existing functions
    * :func:`distinct_combinations` now uses a non-recursive algorithm (thanks to  knutdrand)
    * :func:`pad_none` is now the preferred name for :func:`padnone`, though the latter remains available.
    * :func:`pairwise` will now use the Python standard library implementation on Python 3.10+
    * :func:`sort_together` now accepts a ``key`` argument (thanks to brianmaissy)
    * :func:`seekable` now has a ``peek`` method, and can indicate whether the iterator it's wrapping is exhausted (thanks to gsakkis)
    * :func:`time_limited` can now indicate whether its iterator has expired (thanks to roysmith)
    * The implementation of :func:`unique_everseen` was improved (thanks to plammens)

* Other changes:
    * Various documentation updates (thanks to cthoyt, Evantm, and cyphase)

8.6.0
-----

* New itertools
    * :func:`all_unique` (thanks to brianmaissy)
    * :func:`nth_product` and :func:`nth_permutation` (thanks to N8Brooks)

* Changes to existing itertools
    * :func:`chunked` and :func:`sliced` now accept a ``strict`` parameter (thanks to shlomif and jtwool)

* Other changes
    * Python 3.5 has reached its end of life and is no longer supported.
    * Python 3.9 is officially supported.
    * Various documentation fixes (thanks to timgates42)

8.5.0
-----

* New itertools
    * :func:`windowed_complete` (thanks to MarcinKonowalczyk)

* Changes to existing itertools:
    * The :func:`is_sorted` implementation was improved (thanks to cool-RR)
    * The :func:`groupby_transform` now accepts a ``reducefunc`` parameter.
    * The :func:`last` implementation was improved (thanks to brianmaissy)

* Other changes
    * Various documentation fixes (thanks to craigrosie, samuelstjean, PiCT0)
    * The tests for :func:`distinct_combinations` were improved (thanks to Minabsapi)
    * Automated tests now run on GitHub Actions. All commits now check:
        * That unit tests pass
        * That the examples in docstrings work
        * That test coverage remains high (using `coverage`)
        * For linting errors (using `flake8`)
        * For consistent style (using `black`)
        * That the type stubs work (using `mypy`)
        * That the docs build correctly (using `sphinx`)
        * That packages build correctly (using `twine`)

8.4.0
-----

* New itertools
    * :func:`mark_ends` (thanks to kalekundert)
    * :func:`is_sorted`

* Changes to existing itertools:
    * :func:`islice_extended` can now be used with real slices (thanks to cool-RR)
    * The implementations for :func:`filter_except` and :func:`map_except` were improved (thanks to SergBobrovsky)

* Other changes
    * Automated tests now enforce code style (using `black <https://github.com/psf/black>`__)
    * The various signatures of :func:`islice_extended` and :func:`numeric_range` now appear in the docs (thanks to dsfulf)
    * The test configuration for mypy was updated (thanks to blueyed)


8.3.0
-----

* New itertools
    * :func:`zip_equal` (thanks to frankier and alexmojaki)

* Changes to existing itertools:
    * :func:`split_at`, :func:`split_before`, :func:`split_after`, and :func:`split_when` all got a ``maxsplit`` parameter (thanks to jferard and ilai-deutel)
    * :func:`split_at` now accepts a ``keep_separator`` parameter (thanks to jferard)
    * :func:`distinct_permutations` can now generate ``r``-length permutations (thanks to SergBobrovsky and ilai-deutel)
    * The :func:`windowed` implementation was improved  (thanks to SergBobrovsky)
    * The :func:`spy` implementation was improved (thanks to has2k1)

* Other changes
    * Type stubs are now tested with ``stubtest`` (thanks to ilai-deutel)
    * Tests now run with ``python -m unittest`` instead of ``python setup.py test`` (thanks to jdufresne)

8.2.0
-----

* Bug fixes
    * The .pyi files for typing were updated. (thanks to blueyed and ilai-deutel)

* Changes to existing itertools:
    * :func:`numeric_range` now behaves more like the built-in :func:`range`. (thanks to jferard)
    * :func:`bucket` now allows for enumerating keys. (thanks to alexchandel)
    * :func:`sliced` should work for numpy arrays. (thanks to sswingle)
    * :func:`seekable` now has a ``maxlen`` parameter.

8.1.0
-----

* Bug fixes
    * :func:`partition` works with ``pred=None`` again. (thanks to MSeifert04)

* New itertools
    * :func:`sample` (thanks to tommyod)
    * :func:`nth_or_last` (thanks to d-ryzhikov)

* Changes to existing itertools:
    * The implementation for :func:`divide` was improved. (thanks to jferard)

8.0.2
-----

* Bug fixes
    * The type stub files are now part of the wheel distribution (thanks to keisheiled)

8.0.1
-----

* Bug fixes
    * The type stub files now work for functions imported from the
      root package (thanks to keisheiled)

8.0.0
-----

* New itertools and other additions
    * This library now ships type hints for use with mypy.
      (thanks to ilai-deutel for the implementation, and to gabbard and fmagin for assistance)
    * :func:`split_when` (thanks to jferard)
    * :func:`repeat_last` (thanks to d-ryzhikov)

* Changes to existing itertools:
    * The implementation for :func:`set_partitions` was improved. (thanks to jferard)
    * :func:`partition` was optimized for expensive predicates. (thanks to stevecj)
    * :func:`unique_everseen` and :func:`groupby_transform` were re-factored. (thanks to SergBobrovsky)
    * The implementation for :func:`difference` was improved. (thanks to Jabbey92)

* Other changes
    * Python 3.4 has reached its end of life and is no longer supported.
    * Python 3.8 is officially supported. (thanks to jdufresne)
    * The ``collate`` function has been deprecated.
      It raises a ``DeprecationWarning`` if used, and will be removed in a future release.
    * :func:`one` and :func:`only` now provide more informative error messages. (thanks to gabbard)
    * Unit tests were moved outside of the main package (thanks to jdufresne)
    * Various documentation fixes (thanks to kriomant, gabbard, jdufresne)


7.2.0
-----

* New itertools
    * :func:`distinct_combinations`
    * :func:`set_partitions` (thanks to kbarrett)
    * :func:`filter_except`
    * :func:`map_except`

7.1.0
-----

* New itertools
    * :func:`ichunked` (thanks davebelais and youtux)
    * :func:`only` (thanks jaraco)

* Changes to existing itertools:
    * :func:`numeric_range` now supports ranges specified by
      ``datetime.datetime`` and ``datetime.timedelta`` objects (thanks to MSeifert04 for tests).
    * :func:`difference` now supports an *initial* keyword argument.


* Other changes
    * Various documentation fixes (thanks raimon49, pylang)

7.0.0
-----

* New itertools:
    * :func:`time_limited`
    * :func:`partitions` (thanks to rominf and Saluev)
    * :func:`substrings_indexes` (thanks to rominf)

* Changes to existing itertools:
    * :func:`collapse` now treats ``bytes`` objects the same as ``str`` objects. (thanks to Sweenpet)

The major version update is due to the change in the default behavior of
:func:`collapse`. It now treats ``bytes`` objects the same as ``str`` objects.
This aligns its behavior with :func:`always_iterable`.

.. code-block:: python

    >>> from more_itertools import collapse
    >>> iterable = [[1, 2], b'345', [6]]
    >>> print(list(collapse(iterable)))
    [1, 2, b'345', 6]

6.0.0
-----

* Major changes:
    * Python 2.7 is no longer supported. The 5.0.0 release will be the last
      version targeting Python 2.7.
    * All future releases will target the active versions of Python 3.
      As of 2019, those are Python 3.4 and above.
    * The ``six`` library is no longer a dependency.
    * The :func:`accumulate` function is no longer part of this library. You
      may import a better version from the standard ``itertools`` module.

* Changes to existing itertools:
    * The order of the parameters in :func:`grouper` have changed to match
      the latest recipe in the itertools documentation. Use of the old order
      will be supported in this release, but emit a  ``DeprecationWarning``.
      The legacy behavior will be dropped in a future release. (thanks to jaraco)
    * :func:`distinct_permutations` was improved (thanks to jferard - see also `permutations with unique values <https://stackoverflow.com/questions/6284396/permutations-with-unique-values>`_ at StackOverflow.)
    * An unused parameter was removed from :func:`substrings`. (thanks to pylang)

* Other changes:
    * The docs for :func:`unique_everseen` were improved. (thanks to jferard and MSeifert04)
    * Several Python 2-isms were removed. (thanks to jaraco, MSeifert04, and hugovk)

5.0.0
-----

* New itertools:
    * :func:`split_into` (thanks to rovyko)
    * :func:`unzip` (thanks to bmintz)
    * :func:`substrings` (thanks to pylang)

* Changes to existing itertools:
    * :func:`ilen` was optimized a bit (thanks to MSeifert04, achampion, and  bmintz)
    * :func:`first_true` now returns ``None`` by default. This is the reason for the major version bump - see below. (thanks to sk and OJFord)

* Other changes:
   * Some code for old Python versions was removed (thanks to hugovk)
   * Some documentation mistakes were corrected  (thanks to belm0 and hugovk)
   * Tests now run properly on 32-bit versions of Python (thanks to Millak)
   * Newer versions of CPython and PyPy are now tested against

The major version update is due to the change in the default return value of
:func:`first_true`. It's now ``None``.

.. code-block:: python

    >>> from more_itertools import first_true
    >>> iterable = [0, '', False, [], ()]  # All these are False
    >>> answer = first_true(iterable)
    >>> print(answer)
    None

4.3.0
-----

* New itertools:
    * :func:`last` (thanks to tmshn)
    * :func:`replace` (thanks to pylang)
    * :func:`rlocate` (thanks to jferard and pylang)

* Improvements to existing itertools:
    * :func:`locate` can now search for multiple items

* Other changes:
   * The docs now include a nice table of tools (thanks MSeifert04)

4.2.0
-----

* New itertools:
    * :func:`map_reduce` (thanks to pylang)
    * :func:`prepend` (from the `Python 3.7 docs <https://docs.python.org/3.7/library/itertools.html#itertools-recipes>`_)

* Improvements to existing itertools:
    * :func:`bucket` now complies with PEP 479 (thanks to irmen)

* Other changes:
   * Python 3.7 is now supported (thanks to irmen)
   * Python 3.3 is no longer supported
   * The test suite no longer requires third-party modules to run
   * The API docs now include links to source code

4.1.0
-----

* New itertools:
    * :func:`split_at` (thanks to michael-celani)
    * :func:`circular_shifts` (thanks to hiqua)
    * :func:`make_decorator` - see the blog post `Yo, I heard you like decorators <https://sites.google.com/site/bbayles/index/decorator_factory>`_
      for a tour (thanks to pylang)
    * :func:`always_reversible` (thanks to michael-celani)
    * :func:`nth_combination` (from the `Python 3.7 docs <https://docs.python.org/3.7/library/itertools.html#itertools-recipes>`_)

* Improvements to existing itertools:
    * :func:`seekable` now has an ``elements`` method to return cached items.
    * The performance tradeoffs between :func:`roundrobin` and
      :func:`interleave_longest` are now documented (thanks michael-celani,
      pylang, and MSeifert04)

4.0.1
-----

* No code changes - this release fixes how the docs display on PyPI.

4.0.0
-----

* New itertools:
    * :func:`consecutive_groups` (Based on the example in the `Python 2.4 docs <https://docs.python.org/release/2.4.4/lib/itertools-example.html>`_)
    * :func:`seekable` (If you're looking for how to "reset" an iterator,
      you're in luck!)
    * :func:`exactly_n` (thanks to michael-celani)
    * :func:`run_length.encode` and :func:`run_length.decode`
    * :func:`difference`

* Improvements to existing itertools:
    * The number of items between filler elements in :func:`intersperse` can
      now be specified (thanks to pylang)
    * :func:`distinct_permutations` and :func:`peekable` got some minor
      adjustments (thanks to MSeifert04)
    * :func:`always_iterable` now returns an iterator object. It also now
      allows different types to be considered iterable (thanks to jaraco)
    * :func:`bucket` can now limit the keys it stores in memory
    * :func:`one` now allows for custom exceptions (thanks to kalekundert)

* Other changes:
    * A few typos were fixed (thanks to EdwardBetts)
    * All tests can now be run with ``python setup.py test``

The major version update is due to the change in the return value of :func:`always_iterable`.
It now always returns iterator objects:

.. code-block:: python

    >>> from more_itertools import always_iterable
    # Non-iterable objects are wrapped with iter(tuple(obj))
    >>> always_iterable(12345)
    <tuple_iterator object at 0x7fb24c9488d0>
    >>> list(always_iterable(12345))
    [12345]
    # Iterable objects are wrapped with iter()
    >>> always_iterable([1, 2, 3, 4, 5])
    <list_iterator object at 0x7fb24c948c50>

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
