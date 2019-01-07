from typing import TypeVar, Iterable, Iterator, Sequence, List, Callable, Union, Tuple

T = TypeVar("T")
S = TypeVar("S")
Predicate = Callable[[T], bool]

def chunked(iterable: Iterable[T], n: int) -> Iterator[Iterable[T]]: ...
def sliced(seq: Sequence[T], n: int) -> Iterator[Sequence[T]]: ...
def distribute(
    n: int, iterable: Iterable[T]
) -> List[Iterator[T]]: ...  # Could be a tuple
def split_at(iterable: Iterable[T], pred: Predicate[T]) -> Iterator[List[T]]: ...

# Could return Tuple[Iterator[T],Iterator[T]] with a different implementation
def split_before(iterable: Iterable[T], pred: Predicate[T]) -> List[Iterator[T]]: ...
def split_into(
    iterable: Iterable[T], sizes: Iterable[Union[int, None]]
) -> Iterable[T]: ...
def unzip(iterable: Iterable[Tuple[T, S]]) -> Tuple[Iterable[T], Iterable[S]]: ...

# TODO
# class bucket(Generic[T]):
#     def __init__(self,iterable:Iterable[T],key:Callable[[T],T],validator:Optional[])
