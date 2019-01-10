from collections import Sequence
from typing import (
    Callable,
    Dict,
    Generic,
    Hashable,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
    overload,
    peek,
    seekable,
    Reversible,
    ContextManager,
    Type,
    Any,
)

T = TypeVar("T")
S = TypeVar("S")
U = TypeVar("U")
V = TypeVar("V")
H = TypeVar("H", bound=Hashable)
Predicate = Callable[[T], bool]
KeyFun = Callable[[T], U]

def chunked(iterable: Iterable[T], n: int) -> Iterator[List[T]]: ...
def first(iterable: Iterable[T], default=...): ...
def last(iterable: Any, default=...): ...

class peekable(Iterable[T]):
    def __init__(self, iterable: Iterable[T]) -> None: ...
    def __iter__(self) -> "peekable[T]": ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    @overload
    def peek(self) -> T: ...
    @overload
    def peek(self, default=...) -> T: ...  # TODO: decide on defaults
    def prepend(self, *items: T) -> None: ...
    def __next__(self) -> T: ...
    next: Callable[["peekable"], T] = ...
    def __getitem__(self, index: int) -> T: ...

def collate(
    *iterables: Iterable[T], **kwargs: Union[bool, KeyFun[T, U]]
) -> Iterable[T]: ...
def consumer(func: Any): ...
def ilen(iterable: Iterable[T]) -> int: ...

# TODO : decide default (start is the same case)
def iterate(func: Callable[[T], T], start) -> Iterator[T]: ...
def with_iter(context_manager: ContextManager[Iterable[T]]) -> Iterator[T]: ...
def one(
    iterable: Iterable[T],
    too_short: Optional[Exception] = ...,
    too_long: Optional[Exception] = ...,
) -> T: ...
def distinct_permutations(iterable: Iterable[T]) -> Iterator[Tuple[T, ...]]: ...
def intersperse(e: U, iterable: Iterable[T], n: int = ...) -> Iterator[Union[T, U]]: ...
def unique_to_each(*iterables: Iterable[T]) -> List[List[T]]: ...
@overload
def windowed(
    seq: Sequence[T], n: int, *, step: int = ...
) -> Iterator[Tuple[T, ...]]: ...

# TODO: annotate empty tuple
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

Key_Res = TypeVar("Key_Res")

class bucket(Mapping[Key_Res, Iterable[T]]):
    def __init__(
        self,
        iterable: Iterable[T],
        key: Callable[[T], Key_Res],
        validator: Optional[Predicate[Key_Res]],
    ) -> None: ...
    def __contains__(self, value: Key_Res) -> bool: ...
    def __getitem__(self, value: Key_Res) -> Iterable[T]: ...

class peek(Generic[T]):
    def __init__(self, iterable: Iterable[T]): ...
    def __iter__(self) -> peek[T]: ...
    def __bool__(self) -> bool: ...
    @overload
    def peek(self) -> peek[T]: ...
    @overload
    def peek(self, default: U) -> Union[T, U]: ...
    def prepend(self, *items: T): ...
    def __next__(self) -> T: ...
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> List[T]: ...

def spy(
    iterable: Iterable[T], n: int = ...
) -> Tuple[Tuple[Iterable[T], ...], Iterable[T]]: ...
def interleave(*iterables: Iterable[T]) -> Iterable[T]: ...
def interleave_longest(*iterables: Iterable[T]) -> Iterable[T]: ...

# TODO: Infinitely recursive types?
NestedIterable = Union[T, Iterable[T]]
@overload
def collapse(iterable: Iterable[NestedIterable[T]]) -> Iterator[T]: ...

# TODO: Maybe there's a connection between the type of iterable and the base_type?
@overload
def collapse(
    iterable: Iterable[NestedIterable[T]], base_type: Type[Iterable[U]]
) -> Iterator[Union[T, Iterable[U]]]: ...
@overload
def collapse(
    iterable: Iterable[NestedIterable[T]], *, levels: int
) -> Iterator[NestedIterable[T]]: ...
@overload
def collapse(
    iterable: Iterable[NestedIterable[T]], base_type: Type[Iterable[U]], levels: int
) -> Iterator[Union[NestedIterable[T], U]]: ...
def side_effect(
    func: Any,
    iterable: Any,
    chunk_size: Optional[int] = ...,
    before: Optional[Callable[[], Any]] = ...,
    after: Optional[Callable[[], Any]] = ...,
) -> None: ...
def sliced(seq: Sequence[T], n: int) -> Iterator[Sequence[T]]: ...

# Could return Tuple[Iterator[T],Iterator[T]] with a different implementation
def split_at(iterable: Iterable[T], pred: Predicate[T]) -> Iterator[List[T]]: ...
def split_before(
    iterable: Iterable[T], pred: Predicate[T]
) -> Iterator[Iterator[T]]: ...
def split_after(iterable: Iterable[T], pred: Predicate[T]) -> Iterator[Iterator[T]]: ...
def split_into(
    iterable: Iterable[T], sizes: Iterable[Union[int, None]]
) -> Iterable[T]: ...
def padded(
    iterable: Any,
    fillvalue: Optional[Any] = ...,
    n: Optional[Any] = ...,
    next_multiple: bool = ...,
) -> None: ...
def distribute(
    n: int, iterable: Iterable[T]
) -> List[Iterator[T]]: ...  # Could be a Tuple[Iterator[T], ...]
def stagger(
    iterable: Iterable[T],
    offsets: Tuple[int, ...] = ...,
    longest: bool = ...,
    fillvalue: Optional[U] = ...,
) -> Iterable[Tuple[Union[T, U], ...]]: ...
def zip_offset(*iterables: Iterable[T], **kwargs): ...
def sort_together(
    iterables: Iterable[Iterable[T]],
    key_list: Tuple[KeyFun[T, U]] = ...,
    reverse: bool = ...,
) -> List[Iterator[T]]: ...
def unzip(iterable: Iterable[Tuple[T, S]]) -> Tuple[Iterable[T], Iterable[S]]: ...
def divide(n: int, iterable: Iterable[T]) -> List[T]: ...
def always_iterable(obj: Any, base_type: Any = ...): ...
def adjacent(
    predicate: Predicate[T], iterable: Iterable[T], distance: int = ...
) -> Iterator[Tuple[bool, T]]: ...
def groupby_transform(
    iterable: Any, keyfunc: Optional[Any] = ..., valuefunc: Optional[Any] = ...
): ...
def numeric_range(*args: Any): ...
def count_cycle(iterable: Any, n: Optional[Any] = ...): ...
def locate(iterable: Any, pred: Any = ..., window_size: Optional[Any] = ...): ...
def lstrip(iterable: Any, pred: Any): ...
def rstrip(iterable: Any, pred: Any) -> None: ...
def strip(iterable: Any, pred: Any): ...
def islice_extended(iterable: Any, *args: Any): ...
def always_reversible(iterable: Any): ...
def consecutive_groups(iterable: Any, ordering: Any = ...): ...
def difference(iterable: Any, func: Any = ...): ...

class SequenceView(Sequence):
    def __init__(self, target: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...

class seekable(Generic[T]):
    def __init__(self, iterable: Iterable[T]): ...
    def __iter__(self) -> seekable[T]: ...
    def __next__(self) -> T: ...
    def elements(
        self
    ) -> SequenceView[T]: ...  # TODO: annotate the generic SequenceView
    def seek(self, index: int) -> Iterable[T]: ...

class run_length:
    @staticmethod
    def encode(iterable: Any): ...
    @staticmethod
    def decode(iterable: Any): ...

def exactly_n(iterable: Any, n: Any, predicate: Any = ...): ...
def circular_shifts(iterable: Any): ...
def make_decorator(wrapping_func: Any, result_index: int = ...): ...
@overload
def map_reduce(
    iterable: Iterable[T], keyfunc: Callable[[T], H]
) -> Dict[H, List[T]]: ...
@overload
def map_reduce(
    iterable: Iterable[T], keyfunc: Callable[[T], H], valuefunc: Callable[[T], U]
) -> Dict[H, List[U]]: ...
@overload
def map_reduce(
    iterable: Iterable[T],
    keyfunc: Callable[[T], H],
    *,
    reducefunc: Callable[[List[T]], U]
) -> Dict[H, List[U]]: ...
@overload
def map_reduce(
    iterable: Iterable[T],
    keyfunc: Callable[[T], H],
    valuefunc: Callable[[T], U],
    reducefunc: Callable[[List[U]], V],
) -> Dict[H, V]: ...
def rlocate(iterable: Any, pred: Any = ..., window_size: Optional[Any] = ...): ...
def replace(
    iterable: Any,
    pred: Any,
    substitutes: Any,
    count: Optional[Any] = ...,
    window_size: int = ...,
) -> None: ...
