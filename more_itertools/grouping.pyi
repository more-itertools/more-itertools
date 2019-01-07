from typing import (Callable, Iterable, Iterator, List, Mapping, Optional,
                    Sequence, Tuple, TypeVar, Union)

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

Key_Res = TypeVar("Key_Res")

class bucket(Mapping[Key_Res, Iterable[T]]):
    def __init__(
        self,
        iterable: Iterable[T],
        key: Callable[[T], Key_Res],
        validator: Optional[Predicate[Key_Res]],
    ): ...
    def __contains__(self, value: Key_Res) -> bool: ...
    def __getitem__(self, value: Key_Res) -> Iterable[T]: ...
