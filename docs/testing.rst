=======
Testing
=======

To run install dependencies and run tests, use this command::

    python -m unittest

Multiple Python Versions
========================

To run the tests on all the versions of Python more-itertools supports, install nox::

    pip install nox

Then, run the tests::

    nox -s test
