from typing import Iterable, Iterator, Sequence, Tuple, TypeVar, Union, overload

T = TypeVar("T")
U = TypeVar("U")
@overload
def windowed(
    seq: Sequence[T], n: int, fillvalue: None, step: int = ...
) -> Iterator[Tuple[T, ...]]: ...
@overload
def windowed(
    seq: Sequence[T], n: int, fillvalue: None, step: int = 0
) -> Iterator[Tuple]: ...
@overload
def windowed(
    seq: Sequence[T], n: int, fillvalue: U, step: int = ...
) -> Iterator[Tuple[Union[T, U]]]: ...

# TODO: not sure about this one. also maybe rename it to subiters because it doesn't have to be a string
def substrings(iterable: Iterable[T]) -> Iterator[T]: ...
@overload
def stagger(
    iterable: Iterable[T],
    offsets: Tuple[int, ...] = ...,
    longest: bool = ...,
    fillvalue: None = ...,
) -> Iterable[Tuple[Union[T, None], ...]]: ...
@overload
def stagger(
    iterable: Iterable[T],
    offsets: Tuple[int, ...] = ...,
    longest: bool = ...,
    fillvalue: U = ...,
) -> Iterable[Tuple[Union[T, U], ...]]: ...

# Recipies
def pairwise(iterable: Iterable[T]) -> Iterator[Tuple[T, T]]: ...
