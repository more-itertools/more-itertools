==============
More Itertools
==============

.. image:: https://readthedocs.org/projects/more-itertools/badge/?version=latest
  :target: https://more-itertools.readthedocs.io/en/stable/

Python's ``itertools`` library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In ``more-itertools``
we collect additional building blocks, recipes, and routines for working with
Python iterables.

+------------------------+-------------------------------------------------------------------------------------------------------+
| Grouping               | `chunked <api.html#more_itertools.chunked>`_,                                                         |
|                        | `ichunked <api.html#more_itertools.ichunked>`_,                                                       |
|                        | `sliced <api.html#more_itertools.sliced>`_,                                                           |
|                        | `distribute <api.html#more_itertools.distribute>`_,                                                   |
|                        | `divide <api.html#more_itertools.divide>`_,                                                           |
|                        | `split_at <api.html#more_itertools.split_at>`_,                                                       |
|                        | `split_before <api.html#more_itertools.split_before>`_,                                               |
|                        | `split_after <api.html#more_itertools.split_after>`_,                                                 |
|                        | `split_into <api.html#more_itertools.split_into>`_,                                                   |
|                        | `split_when <api.html#more_itertools.split_when>`_,                                                   |
|                        | `bucket <api.html#more_itertools.bucket>`_,                                                           |
|                        | `unzip <api.html#more_itertools.unzip>`_,                                                             |
|                        | `grouper <api.html#more_itertools.grouper>`_,                                                         |
|                        | `partition <api.html#more_itertools.partition>`_                                                      |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Lookahead and lookback | `spy <api.html#more_itertools.spy>`_,                                                                 |
|                        | `peekable <api.html#more_itertools.peekable>`_,                                                       |
|                        | `seekable <api.html#more_itertools.seekable>`_                                                        |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Windowing              | `windowed <api.html#more_itertools.windowed>`_,                                                       |
|                        | `substrings <api.html#more_itertools.substrings>`_,                                                   |
|                        | `substrings_indexes <api.html#more_itertools.substrings_indexes>`_,                                   |
|                        | `stagger <api.html#more_itertools.stagger>`_,                                                         |
|                        | `windowed_complete <api.html#more_itertools.windowed_complete>`_,                                     |
|                        | `pairwise <api.html#more_itertools.pairwise>`_                                                        |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Augmenting             | `count_cycle <api.html#more_itertools.count_cycle>`_,                                                 |
|                        | `intersperse <api.html#more_itertools.intersperse>`_,                                                 |
|                        | `padded <api.html#more_itertools.padded>`_,                                                           |
|                        | `mark_ends <api.html#more_itertools.mark_ends>`_,                                                     |
|                        | `repeat_last <api.html#more_itertools.repeat_last>`_,                                                 |
|                        | `adjacent <api.html#more_itertools.adjacent>`_,                                                       |
|                        | `groupby_transform <api.html#more_itertools.groupby_transform>`_,                                     |
|                        | `padnone <api.html#more_itertools.padnone>`_,                                                         |
|                        | `ncycles <api.html#more_itertools.ncycles>`_                                                          |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Combining              | `collapse <api.html#more_itertools.collapse>`_,                                                       |
|                        | `sort_together <api.html#more_itertools.sort_together>`_,                                             |
|                        | `interleave <api.html#more_itertools.interleave>`_,                                                   |
|                        | `interleave_longest <api.html#more_itertools.interleave_longest>`_,                                   |
|                        | `interleave_evenly <api.html#more_itertools.interleave_evenly>`_,                                     |
|                        | `zip_offset <api.html#more_itertools.zip_offset>`_,                                                   |
|                        | `zip_equal <api.html#more_itertools.zip_equal>`_,                                                     |
|                        | `dotproduct <api.html#more_itertools.dotproduct>`_,                                                   |
|                        | `convolve <api.html#more_itertools.convolve>`_,                                                       |
|                        | `flatten <api.html#more_itertools.flatten>`_,                                                         |
|                        | `roundrobin <api.html#more_itertools.roundrobin>`_,                                                   |
|                        | `prepend <api.html#more_itertools.prepend>`_,                                                         |
|                        | `value_chain <api.html#more_itertools.value_chain>`_                                                  |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Summarizing            | `ilen <api.html#more_itertools.ilen>`_,                                                               |
|                        | `unique_to_each <api.html#more_itertools.unique_to_each>`_,                                           |
|                        | `sample <api.html#more_itertools.sample>`_,                                                           |
|                        | `consecutive_groups <api.html#more_itertools.consecutive_groups>`_,                                   |
|                        | `run_length <api.html#more_itertools.run_length>`_,                                                   |
|                        | `map_reduce <api.html#more_itertools.map_reduce>`_,                                                   |
|                        | `exactly_n <api.html#more_itertools.exactly_n>`_,                                                     |
|                        | `is_sorted <api.html#more_itertools.is_sorted>`_,                                                     |
|                        | `all_equal <api.html#more_itertools.all_equal>`_,                                                     |
|                        | `all_unique <api.html#more_itertools.all_unique>`_,                                                   |
|                        | `first_true <api.html#more_itertools.first_true>`_,                                                   |
|                        | `quantify <api.html#more_itertools.quantify>`_                                                        |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Selecting              | `islice_extended <api.html#more_itertools.islice_extended>`_,                                         |
|                        | `first <api.html#more_itertools.first>`_,                                                             |
|                        | `last <api.html#more_itertools.last>`_,                                                               |
|                        | `one <api.html#more_itertools.one>`_,                                                                 |
|                        | `only <api.html#more_itertools.only>`_,                                                               |
|                        | `strip <api.html#more_itertools.strip>`_,                                                             |
|                        | `lstrip <api.html#more_itertools.lstrip>`_,                                                           |
|                        | `rstrip <api.html#more_itertools.rstrip>`_,                                                           |
|                        | `filter_except <api.html#more_itertools.filter_except>`_                                              |
|                        | `map_except <api.html#more_itertools.map_except>`_                                                    |
|                        | `nth_or_last <api.html#more_itertools.nth_or_last>`_,                                                 |
|                        | `nth <api.html#more_itertools.nth>`_,                                                                 |
|                        | `take <api.html#more_itertools.take>`_,                                                               |
|                        | `tail <api.html#more_itertools.tail>`_,                                                               |
|                        | `unique_everseen <api.html#more_itertoo ls.unique_everseen>`_,                                        |
|                        | `unique_justseen <api.html#more_itertools.unique_justseen>`_                                          |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Combinatorics          | `distinct_permutations <api.html#more_itertools.distinct_permutations>`_,                             |
|                        | `distinct_combinations <api.html#more_itertools.distinct_combinations>`_,                             |
|                        | `circular_shifts <api.html#more_itertools.circular_shifts>`_,                                         |
|                        | `partitions <api.html#more_itertools.partitions>`_,                                                   |
|                        | `set_partitions <api.html#more_itertools.set_partitions>`_,                                           |
|                        | `product_index <api.html#more_itertools.product_index>`_,                                             |
|                        | `combination_index <api.html#more_itertools.combination_index>`_,                                     |
|                        | `permutation_index <api.html#more_itertools.permutation_index>`_,                                     |
|                        | `powerset <api.html#more_itertools.powerset>`_,                                                       |
|                        | `random_product <api.html#more_itertools.random_product>`_,                                           |
|                        | `random_permutation <api.html#more_itertools.random_permutation>`_,                                   |
|                        | `random_combination <api.html#more_itertools.random_combination>`_,                                   |
|                        | `random_combination_with_replacement <api.html#more_itertools.random_combination_with_replacement>`_, |
|                        | `nth_product <api.html#more_itertools.nth_product>`_,                                                 |
|                        | `nth_permutation <api.html#more_itertools.nth_permutation>`_,                                         |
|                        | `nth_combination <api.html#more_itertools.nth_combination>`_                                          |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Wrapping               | `always_iterable <api.html#more_itertools.always_iterable>`_,                                         |
|                        | `always_reversible <api.html#more_itertools.always_reversible>`_,                                     |
|                        | `countable <api.html#more_itertools.countable>`_,                                                     |
|                        | `consumer <api.html#more_itertools.consumer>`_,                                                       |
|                        | `with_iter <api.html#more_itertools.with_iter>`_,                                                     |
|                        | `iter_except <api.html#more_itertools.iter_except>`_                                                  |
+------------------------+-------------------------------------------------------------------------------------------------------+
| Others                 | `locate <api.html#more_itertools.locate>`_,                                                           |
|                        | `rlocate <api.html#more_itertools.rlocate>`_,                                                         |
|                        | `replace <api.html#more_itertools.replace>`_,                                                         |
|                        | `numeric_range <api.html#more_itertools.numeric_range>`_,                                             |
|                        | `side_effect <api.html#more_itertools.side_effect>`_,                                                 |
|                        | `iterate <api.html#more_itertools.iterate>`_,                                                         |
|                        | `difference <api.html#more_itertools.difference>`_,                                                   |
|                        | `make_decorator <api.html#more_itertools.make_decorator>`_,                                           |
|                        | `SequenceView <api.html#more_itertools.SequenceView>`_,                                               |
|                        | `time_limited <api.html#more_itertools.time_limited>`_,                                               |
|                        | `consume <api.html#more_itertools.consume>`_,                                                         |
|                        | `tabulate <api.html#more_itertools.tabulate>`_,                                                       |
|                        | `repeatfunc <api.html#more_itertools.repeatfunc>`_                                                    |
+------------------------+-------------------------------------------------------------------------------------------------------+


Getting started
===============

To get started, install the library with `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: shell

    pip install more-itertools

The recipes from the `itertools docs <https://docs.python.org/3/library/itertools.html#itertools-recipes>`_
are included in the top-level package:

.. code-block:: python

    >>> from more_itertools import flatten
    >>> iterable = [(0, 1), (2, 3)]
    >>> list(flatten(iterable))
    [0, 1, 2, 3]

Several new recipes are available as well:

.. code-block:: python

    >>> from more_itertools import chunked
    >>> iterable = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    >>> list(chunked(iterable, 3))
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    >>> from more_itertools import spy
    >>> iterable = (x * x for x in range(1, 6))
    >>> head, iterable = spy(iterable, n=3)
    >>> list(head)
    [1, 4, 9]
    >>> list(iterable)
    [1, 4, 9, 16, 25]



For the full listing of functions, see the `API documentation <api.html>`_.


Links elsewhere
===============

Blog posts about ``more-itertools``:

* `Yo, I heard you like decorators <https://www.bbayles.com/index/decorator_factory>`__
* `Tour of Python Itertools <https://martinheinz.dev/blog/16>`__ (`Alternate <https://dev.to/martinheinz/tour-of-python-itertools-4122>`__)


Development
===========

``more-itertools`` is maintained by `@erikrose <https://github.com/erikrose>`_
and `@bbayles <https://github.com/bbayles>`_, with help from `many others <https://github.com/more-itertools/more-itertools/graphs/contributors>`_.
If you have a problem or suggestion, please file a bug or pull request in this
repository. Thanks for contributing!
