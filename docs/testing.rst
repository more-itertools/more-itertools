=======
Testing
=======

To run the test suite, use this command::

    python -m unittest

Concurrency tests
=================

The concurrency tests are included in the regular test suite. To run just the
``concurrent_tee`` tests, use::

    python -m unittest tests.test_more.TestConcurrentTee

The contention test uses an event to ensure that two consumers reach the same
uncached item before the source yields it. This checks that waiting consumers
reuse the cached item rather than advancing the source again. The waits have
timeouts, and exceptions raised in worker threads are reported by the test.

Multiple Python Versions
========================

To run the tests on all the versions of Python more-itertools supports, install
tox::

    pip install tox

Then, run the tests::

    tox
