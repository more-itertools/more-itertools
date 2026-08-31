"""Regression test for one() handling of custom exceptions and faulty __repr__."""
import pytest
from itertools import count
from more_itertools import one


class OpinionatedError(Exception):
    """An exception whose __bool__ always returns False."""
    def __bool__(self):
        return False


class OpinionatedObject:
    """An object whose __repr__ raises."""
    def __repr__(self):
        raise NotImplementedError("No representation without taxation!")


def test_one_too_long_with_opinionated_exception():
    """When too_long is an exception instance with __bool__ returning False,
    one() should raise that exception, not ValueError."""
    it = count()
    exc = OpinionatedError()
    with pytest.raises(OpinionatedError):
        one(it, too_long=exc)


def test_one_too_short_with_opinionated_exception():
    """When too_short is an exception instance with __bool__ returning False,
    one() should raise that exception, not ValueError."""
    it = []
    exc = OpinionatedError()
    with pytest.raises(OpinionatedError):
        one(it, too_short=exc)


def test_one_too_long_with_faulty_repr():
    """When items have faulty __repr__, one() should raise too_long exception,
    not the __repr__ error."""
    it = (OpinionatedObject() for _ in count())
    with pytest.raises(OverflowError):
        one(it, too_long=OverflowError)
