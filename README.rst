==============
More Itertools
==============

I love itertools; it's one of the most beautiful, composable standard libs.
"Aha! I have an iteration problem here; I'm sure there is an itertools routine
that fits it perfectly" oft passes my lips. My confidence is typically
well-placed, but sometimes, neither itertools nor the recipes included in its
docs do quite what I need.

Here I've collected several routines I've reached for but not found. Since
these are deceptively tricky to get right, I thought I'd wrap them up into a
library. Enjoy! Any additions are welcome; just file a pull request.


License
=======

More Itertools is under the MIT License. See the LICENSE file.


Run the tests
=============

This uses nose for tests. First, install nose::

    pip install nose

Then, run the tests like this::

    nosetests

It should also be possible to say ``python setup.py test``. However, some part
of the test runner throws an error after the tests pass.


Version History
===============

1.1
    * Added ``first`` function.

1.0
    * Initial release, with ``collate``, ``peekable``, and ``chunked``. Could
      really use better docs.
