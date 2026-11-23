=======
Testing
=======

From the repository root, run the test suite with Python's built-in
``unittest`` runner (no extra dependencies are required)::

    python -m unittest

To run just the tests for a function, pass the dotted path to its test class.
For example, to test ``chunked``::

    python -m unittest tests.test_more.ChunkedTests

Multiple Python Versions
========================

To run the tests on all the versions of Python more-itertools supports, install
tox::

    pip install tox

Then, run the tests::

    tox
