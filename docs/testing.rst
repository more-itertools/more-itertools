=======
Testing
=======

more-itertools uses nose for its tests. First, install nose::

    pip install nose

Then, run the tests like this::

    nosetests --with-doctest


Multiple Python Versions
========================

To run the tests on all the versions of Python more-itertools supports, install
tox::

    pip install tox

Then, run the tests::

    tox
