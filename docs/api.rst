=============
API Reference
=============

.. automodule:: more_itertools

Grouping
========

These tools yield groups of items from a source iterable.

----

**New itertools**

.. autofunction:: chunked
.. autofunction:: ichunked
.. autofunction:: sliced
.. autofunction:: distribute
.. autofunction:: divide
.. autofunction:: split_at
.. autofunction:: split_before
.. autofunction:: split_after
.. autofunction:: split_into
.. autofunction:: split_when
.. autofunction:: bucket
.. autofunction:: unzip

----

**Itertools recipes**

.. autofunction:: grouper
.. autofunction:: partition


Lookahead and lookback
======================

These tools peek at an iterable's values without advancing it.

----

**New itertools**


.. autofunction:: spy
.. autoclass:: peekable
.. autoclass:: seekable


Windowing
=========

These tools yield windows of items from an iterable.

----

**New itertools**

.. autofunction:: windowed
.. autofunction:: substrings
.. autofunction:: substrings_indexes
.. autofunction:: stagger

----

**Itertools recipes**

.. autofunction:: pairwise


Augmenting
==========

These tools yield items from an iterable, plus additional data.

----

**New itertools**

.. autofunction:: count_cycle
.. autofunction:: intersperse
.. autofunction:: padded
.. autofunction:: repeat_last
.. autofunction:: adjacent
.. autofunction:: groupby_transform

----

**Itertools recipes**

.. autofunction:: padnone
.. autofunction:: ncycles


Combining
=========

These tools combine multiple iterables.

----

**New itertools**

.. autofunction:: collapse
.. autofunction:: sort_together
.. autofunction:: interleave
.. autofunction:: interleave_longest
.. autofunction:: zip_offset(*iterables, offsets, longest=False, fillvalue=None)

----

**Itertools recipes**

.. autofunction:: dotproduct
.. autofunction:: flatten
.. autofunction:: roundrobin
.. autofunction:: prepend


Summarizing
===========

These tools return summarized or aggregated data from an iterable.

----

**New itertools**

.. autofunction:: ilen
.. autofunction:: first(iterable[, default])
.. autofunction:: last(iterable[, default])
.. autofunction:: one(iterable, too_short=ValueError, too_long=ValueError)
.. autofunction:: only(iterable, default=None, too_long=ValueError)
.. autofunction:: unique_to_each
.. autofunction:: locate(iterable, pred=bool, window_size=None)
.. autofunction:: rlocate(iterable, pred=bool, window_size=None)
.. autofunction:: consecutive_groups(iterable, ordering=lambda x: x)
.. autofunction:: exactly_n(iterable, n, predicate=bool)
.. autoclass:: run_length
.. autofunction:: map_reduce

----

**Itertools recipes**

.. autofunction:: all_equal
.. autofunction:: first_true
.. autofunction:: nth
.. autofunction:: quantify(iterable, pred=bool)


Selecting
=========

These tools yield certain items from an iterable.

----

**New itertools**

.. autofunction:: islice_extended(start, stop, step)
.. autofunction:: strip
.. autofunction:: lstrip
.. autofunction:: rstrip
.. autofunction:: filter_except
.. autofunction:: map_except

----

**Itertools recipes**

.. autofunction:: take
.. autofunction:: tail
.. autofunction:: unique_everseen
.. autofunction:: unique_justseen


Combinatorics
=============

These tools yield combinatorial arrangements of items from iterables.

----

**New itertools**

.. autofunction:: distinct_permutations
.. autofunction:: distinct_combinations
.. autofunction:: circular_shifts
.. autofunction:: partitions
.. autofunction:: set_partitions

----

**Itertools recipes**

.. autofunction:: powerset
.. autofunction:: random_product
.. autofunction:: random_permutation
.. autofunction:: random_combination
.. autofunction:: random_combination_with_replacement
.. autofunction:: nth_combination


Wrapping
========

These tools provide wrappers to smooth working with objects that produce or
consume iterables.

----

**New itertools**

.. autofunction:: always_iterable
.. autofunction:: consumer
.. autofunction:: with_iter

----

**Itertools recipes**

.. autofunction:: iter_except


Others
======

**New itertools**

.. autofunction:: replace
.. autofunction:: numeric_range(start, stop, step)
.. autofunction:: always_reversible
.. autofunction:: side_effect
.. autofunction:: iterate
.. autofunction:: difference(iterable, func=operator.sub)
.. autofunction:: make_decorator
.. autoclass:: SequenceView
.. autofunction:: time_limited

----

**Itertools recipes**

.. autofunction:: consume
.. autofunction:: tabulate
.. autofunction:: repeatfunc
