==============
More Itertools
==============

.. image:: https://readthedocs.org/projects/more-itertools/badge/?version=latest
  :target: https://more-itertools.readthedocs.io/en/stable/

Python's ``itertools`` library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In ``more-itertools``
we collect additional building blocks, recipes, and routines for working with
Python iterables.

+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Grouping               | `chunked <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.chunked>`_,                                                                               |
|                        | `ichunked <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.ichunked>`_,                                                                             |
|                        | `chunked_even <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.chunked_even>`_,                                                                     |
|                        | `sliced <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.sliced>`_,                                                                                 |
|                        | `constrained_batches <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.constrained_batches>`_,                                                       |
|                        | `distribute <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.distribute>`_,                                                                         |
|                        | `divide <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.divide>`_,                                                                                 |
|                        | `split_at <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.split_at>`_,                                                                             |
|                        | `split_before <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.split_before>`_,                                                                     |
|                        | `split_after <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.split_after>`_,                                                                       |
|                        | `split_into <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.split_into>`_,                                                                         |
|                        | `split_when <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.split_when>`_,                                                                         |
|                        | `bucket <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.bucket>`_,                                                                                 |
|                        | `unzip <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.unzip>`_,                                                                                   |
|                        | `batched <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.batched>`_,                                                                               |
|                        | `grouper <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.grouper>`_,                                                                               |
|                        | `partition <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.partition>`_,                                                                           |
|                        | `transpose <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.transpose>`_                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lookahead and lookback | `spy <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.spy>`_,                                                                                       |
|                        | `peekable <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.peekable>`_,                                                                             |
|                        | `seekable <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.seekable>`_                                                                              |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Windowing              | `windowed <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.windowed>`_,                                                                             |
|                        | `substrings <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.substrings>`_,                                                                         |
|                        | `substrings_indexes <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.substrings_indexes>`_,                                                         |
|                        | `stagger <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.stagger>`_,                                                                               |
|                        | `windowed_complete <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.windowed_complete>`_,                                                           |
|                        | `pairwise <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.pairwise>`_,                                                                             |
|                        | `triplewise <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.triplewise>`_,                                                                         |
|                        | `sliding_window <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.sliding_window>`_,                                                                 |
|                        | `subslices <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.subslices>`_                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Augmenting             | `count_cycle <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.count_cycle>`_,                                                                       |
|                        | `intersperse <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.intersperse>`_,                                                                       |
|                        | `padded <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.padded>`_,                                                                                 |
|                        | `repeat_each <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.repeat_each>`_,                                                                       |
|                        | `mark_ends <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.mark_ends>`_,                                                                           |
|                        | `repeat_last <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.repeat_last>`_,                                                                       |
|                        | `adjacent <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.adjacent>`_,                                                                             |
|                        | `groupby_transform <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.groupby_transform>`_,                                                           |
|                        | `pad_none <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.pad_none>`_,                                                                             |
|                        | `ncycles <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.ncycles>`_                                                                                |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Combining              | `collapse <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.collapse>`_,                                                                             |
|                        | `sort_together <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.sort_together>`_,                                                                   |
|                        | `interleave <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.interleave>`_,                                                                         |
|                        | `interleave_longest <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.interleave_longest>`_,                                                         |
|                        | `interleave_evenly <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.interleave_evenly>`_,                                                           |
|                        | `zip_offset <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.zip_offset>`_,                                                                         |
|                        | `zip_equal <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.zip_equal>`_,                                                                           |
|                        | `zip_broadcast <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.zip_broadcast>`_,                                                                   |
|                        | `flatten <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.flatten>`_,                                                                               |
|                        | `roundrobin <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.roundrobin>`_,                                                                         |
|                        | `prepend <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.prepend>`_,                                                                               |
|                        | `value_chain <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.value_chain>`_,                                                                       |
|                        | `partial_product <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.partial_product>`_                                                                |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Summarizing            | `ilen <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.ilen>`_,                                                                                     |
|                        | `unique_to_each <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.unique_to_each>`_,                                                                 |
|                        | `sample <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.sample>`_,                                                                                 |
|                        | `consecutive_groups <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.consecutive_groups>`_,                                                         |
|                        | `run_length <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.run_length>`_,                                                                         |
|                        | `map_reduce <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.map_reduce>`_,                                                                         |
|                        | `join_mappings <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.join_mappings>`_,                                                                   |
|                        | `exactly_n <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.exactly_n>`_,                                                                           |
|                        | `is_sorted <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.is_sorted>`_,                                                                           |
|                        | `all_equal <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.all_equal>`_,                                                                           |
|                        | `all_unique <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.all_unique>`_,                                                                         |
|                        | `minmax <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.minmax>`_,                                                                                 |
|                        | `first_true <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.first_true>`_,                                                                         |
|                        | `quantify <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.quantify>`_,                                                                             |
|                        | `iequals <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iequals>`_                                                                                |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Selecting              | `islice_extended <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.islice_extended>`_,                                                               |
|                        | `first <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.first>`_,                                                                                   |
|                        | `last <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.last>`_,                                                                                     |
|                        | `one <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.one>`_,                                                                                       |
|                        | `only <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.only>`_,                                                                                     |
|                        | `strictly_n <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.strictly_n>`_,                                                                         |
|                        | `strip <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.strip>`_,                                                                                   |
|                        | `lstrip <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.lstrip>`_,                                                                                 |
|                        | `rstrip <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.rstrip>`_,                                                                                 |
|                        | `filter_except <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.filter_except>`_,                                                                   |
|                        | `map_except <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.map_except>`_,                                                                         |
|                        | `filter_map <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.filter_map>`_,                                                                         |
|                        | `iter_suppress <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iter_suppress>`_,                                                                   |
|                        | `nth_or_last <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth_or_last>`_,                                                                       |
|                        | `unique_in_window <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.unique_in_window>`_,                                                             |
|                        | `before_and_after <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.before_and_after>`_,                                                             |
|                        | `nth <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth>`_,                                                                                       |
|                        | `take <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.take>`_,                                                                                     |
|                        | `tail <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.tail>`_,                                                                                     |
|                        | `unique_everseen <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.unique_everseen>`_,                                                               |
|                        | `unique_justseen <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.unique_justseen>`_,                                                               |
|                        | `unique <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.unique>`_,                                                                                 |
|                        | `duplicates_everseen <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.duplicates_everseen>`_,                                                       |
|                        | `duplicates_justseen <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.duplicates_justseen>`_,                                                       |
|                        | `classify_unique <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.classify_unique>`_,                                                               |
|                        | `longest_common_prefix <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.longest_common_prefix>`_,                                                   |
|                        | `takewhile_inclusive <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.takewhile_inclusive>`_                                                        |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Math                   | `dft <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.dft>`_,                                                                                       |
|                        | `idft <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.idft>`_,                                                                                     |
|                        | `convolve <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.convolve>`_,                                                                             |
|                        | `dotproduct <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.dotproduct>`_,                                                                         |
|                        | `matmul <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.matmul>`_,                                                                                 |
|                        | `polynomial_from_roots <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.polynomial_from_roots>`_,                                                   |
|                        | `polynomial_derivative <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.polynomial_derivative>`_,                                                   |
|                        | `polynomial_eval <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.polynomial_eval>`_,                                                               |
|                        | `sum_of_squares <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.sum_of_squares>`_,                                                                 |
|                        | `running_median <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.running_median>`_,                                                                 |
|                        | `totient <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.totient>`_                                                                                |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Integer math           | `factor <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.factor>`_,                                                                                 |
|                        | `is_prime <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.is_prime>`_,                                                                             |
|                        | `multinomial <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.multinomial>`_,                                                                       |
|                        | `nth_prime <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth_prime>`_,                                                                           |
|                        | `sieve <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.sieve>`_                                                                                    |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Combinatorics          | `circular_shifts <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.circular_shifts>`_,                                                               |
|                        | `derangements <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.derangements>`_,                                                                     |
|                        | `gray_product  <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.gray_product>`_,                                                                    |
|                        | `outer_product  <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.outer_product>`_,                                                                  |
|                        | `partitions <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.partitions>`_,                                                                         |
|                        | `set_partitions <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.set_partitions>`_,                                                                 |
|                        | `powerset <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.powerset>`_,                                                                             |
|                        | `powerset_of_sets <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.powerset_of_sets>`_                                                              |
|                        +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                        | `distinct_combinations <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.distinct_combinations>`_,                                                   |
|                        | `distinct_permutations <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.distinct_permutations>`_                                                    |
|                        +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                        | `combination_index <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.combination_index>`_,                                                           |
|                        | `combination_with_replacement_index <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.combination_with_replacement_index>`_,                         |
|                        | `permutation_index <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.permutation_index>`_,                                                           |
|                        | `product_index <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.product_index>`_                                                                    |
|                        +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                        | `nth_combination <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth_combination>`_,                                                               |
|                        | `nth_combination_with_replacement <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth_combination_with_replacement>`_,                             |
|                        | `nth_permutation <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth_permutation>`_,                                                               |
|                        | `nth_product <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth_product>`_                                                                        |
|                        +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                        | `random_combination <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.random_combination>`_,                                                         |
|                        | `random_combination_with_replacement <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.random_combination_with_replacement>`_,                       |
|                        | `random_permutation <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.random_permutation>`_,                                                         |
|                        | `random_product <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.random_product>`_                                                                  |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wrapping               | `always_iterable <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.always_iterable>`_,                                                               |
|                        | `always_reversible <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.always_reversible>`_,                                                           |
|                        | `countable <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.countable>`_,                                                                           |
|                        | `consumer <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.consumer>`_,                                                                             |
|                        | `with_iter <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.with_iter>`_,                                                                           |
|                        | `iter_except <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iter_except>`_                                                                        |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Others                 | `locate <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.locate>`_,                                                                                 |
|                        | `rlocate <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.rlocate>`_,                                                                               |
|                        | `replace <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.replace>`_,                                                                               |
|                        | `numeric_range <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.numeric_range>`_,                                                                   |
|                        | `side_effect <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.side_effect>`_,                                                                       |
|                        | `iterate <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iterate>`_,                                                                               |
|                        | `loops <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.loops>`_,                                                                                   |
|                        | `difference <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.difference>`_,                                                                         |
|                        | `make_decorator <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.make_decorator>`_,                                                                 |
|                        | `SequenceView <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.SequenceView>`_,                                                                     |
|                        | `time_limited <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.time_limited>`_,                                                                     |
|                        | `map_if <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.map_if>`_,                                                                                 |
|                        | `iter_index <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iter_index>`_,                                                                         |
|                        | `consume <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.consume>`_,                                                                               |
|                        | `tabulate <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.tabulate>`_,                                                                             |
|                        | `repeatfunc <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.repeatfunc>`_,                                                                         |
|                        | `reshape <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.reshape>`_,                                                                               |
|                        | `doublestarmap <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.doublestarmap>`_                                                                    |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


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



For the full listing of functions, see the `API documentation <https://more-itertools.readthedocs.io/en/stable/api.html>`_.


Links elsewhere
===============

Blog posts about ``more-itertools``:

* `Yo, I heard you like decorators <https://www.bbayles.com/index/decorator_factory>`__
* `Tour of Python Itertools <https://martinheinz.dev/blog/16>`__ (`Alternate <https://dev.to/martinheinz/tour-of-python-itertools-4122>`__)
* `Real-World Python More Itertools <https://python.plainenglish.io/real-world-more-itertools-gideons-blog-a3901c607550>`_


Development
===========

``more-itertools`` is maintained by `@erikrose <https://github.com/erikrose>`_
and `@bbayles <https://github.com/bbayles>`_, with help from `many others <https://github.com/more-itertools/more-itertools/graphs/contributors>`_.
If you have a problem or suggestion, please file a bug or pull request in this
repository. Thanks for contributing!


Version History
===============

The version history can be found in `documentation <https://more-itertools.readthedocs.io/en/stable/versions.html>`_.
