==============
More Itertools
==============

I love itertools; it's one of the most beautiful, composable standard libs.
"Aha! I have an iteration problem here; I'm sure there is an itertools routine
that fits it perfectly" oft passes my lips. Often, my confidence is
well-placed, but sometimes, neither itertools nor the recipes included in its
docs do quite what I need.

Here I've collected several routines I've reached for but not found. Since
these are deceptively tricky to get right, I thought I'd wrap them up into a
library. Enjoy! Any additions are welcome; just file a pull request.


The Routines
============

``chunked(iterable, n)``
    Break an iterable into tuples of a given length.

    chunked([1, 2, 3, 4, 5, 6, 7], 3) --> [(1, 2, 3), (4, 5, 6), (7,)]

    If the length of ``iterable`` is not evenly divisible by ``n``, the last
    returned tuple will be shorter.

``peekable(iterable)``
    Wrapper for an iterator to allow 1-item lookahead
    
    ``peekable(iterator).peek()`` returns the value that will next pop out of
    ``next()``.

``collate(*iterables[, key=<key function>, reverse=<bool>])``
    Return an iterable ordered collation of the already-sorted items
    from each of ``iterables``, compared by kwarg ``key``.

    If ``reverse=True`` is passed, iterables must return their results in
    descending order rather than ascending.


License
=======

More Itertools is under the MIT License. See the LICENSE file.


Version History
===============

1.0
    * Initial release, with ``collate``, ``peekable``, and ``chunked``. Could
      really use better docs.
