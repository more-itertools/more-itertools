=======
Testing
=======

more-itertools uses nose for its tests. First, install nose::

    pip install nose

Then, run the tests like this::

    nosetests

It should also be possible to say ``python setup.py test``. However, some part
of the test runner throws an error after the tests pass.


Multiple Python Versions
========================

To run the tests on all the versions of Python more-itertools supports, install tox::

    pip install tox

Then, run the tests::

    tox
