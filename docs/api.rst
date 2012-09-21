=============
API Reference
=============

Though these routines are listed as living under the ``more`` and ``recipes``
submodules, you should just import them from ``more_itertools`` directly.


New Routines
============

.. automodule:: more_itertools.more

    .. autofunction:: chunked
    .. autofunction:: collate(*iterables, key=lambda a: a, reverse=False)
    .. autofunction:: consumer
    .. autofunction:: first(iterable[, default])
    .. autofunction:: ilen
    .. autoclass:: peekable


Itertools Recipes
=================

.. automodule:: more_itertools.recipes
   :members:
