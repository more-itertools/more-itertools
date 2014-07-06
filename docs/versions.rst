===============
Version History
===============

2.4
    * Added ``total_product`` and ``specific_product``. (Thanks, Andy Hawkins of BombSquad!)

2.3
    * Added ``one`` from ``jaraco.util.itertools``. (Thanks, jaraco!)
    * Added ``distinct_permutations``. (Thanks, Bo Bayles!)

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
