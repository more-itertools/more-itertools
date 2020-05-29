"""Stubs for more_itertools.more"""

from typing import (
    Any,
    Callable,
    Container,
    Dict,
    Generic,
    Hashable,
    Iterable,
    Iterator,
    List,
    Optional,
    Reversible,
    Sequence,
    Sized,
    Tuple,
    Union,
    TypeVar,
    type_check_only,
)
from typing_extensions import ContextManager, Protocol, Type, overload

# Type and type variable definitions
_T = TypeVar('_T')
_U = TypeVar('_U')
_V = TypeVar('_V')
_W = TypeVar('_W')
_T_co = TypeVar('_T_co', covariant=True)
_GenFn = TypeVar('_GenFn', bound=Callable[..., Iterator[object]])
_Raisable = Union[BaseException, 'Type[BaseException]']
@type_check_only
class _SizedIterable(Protocol[_T_co], Sized, Iterable[_T_co]): ...

@type_check_only
class _SizedReversible(Protocol[_T_co], Sized, Reversible[_T_co]): ...

def chunked(iterable: Iterable[_T], n: int) -> Iterator[List[_T]]: ...
@overload
def first(iterable: Iterable[_T]) -> _T: ...
@overload
def first(iterable: Iterable[_T], default: _U) -> Union[_T, _U]: ...
@overload
def last(iterable: Iterable[_T]) -> _T: ...
@overload
def last(iterable: Iterable[_T], default: _U) -> Union[_T, _U]: ...
@overload
def nth_or_last(iterable: Iterable[_T], n: int) -> _T: ...
@overload
def nth_or_last(
    iterable: Iterable[_T], n: int, default: _U
) -> Union[_T, _U]: ...

class peekable(Generic[_T], Iterator[_T]):
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    def __iter__(self) -> peekable[_T]: ...
    def __bool__(self) -> bool: ...
    @overload
    def peek(self) -> _T: ...
    @overload
    def peek(self, default: _U) -> Union[_T, _U]: ...
    def prepend(self, *items: _T) -> None: ...
    def __next__(self) -> _T: ...
    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, index: slice) -> List[_T]: ...

def collate(*iterables: Iterable[_T], **kwargs: Any) -> Iterable[_T]: ...
def consumer(func: _GenFn) -> _GenFn: ...
def ilen(iterable: Iterable[object]) -> int: ...
def iterate(func: Callable[[_T], _T], start: _T) -> Iterator[_T]: ...
def with_iter(
    context_manager: ContextManager[Iterable[_T]],
) -> Iterator[_T]: ...
def one(
    iterable: Iterable[_T],
    too_short: Optional[_Raisable] = ...,
    too_long: Optional[_Raisable] = ...,
) -> _T: ...
def distinct_permutations(
    iterable: Iterable[_T], r: Optional[int] = ...
) -> Iterator[Tuple[_T, ...]]: ...
def intersperse(
    e: _U, iterable: Iterable[_T], n: int = ...
) -> Iterator[Union[_T, _U]]: ...
def unique_to_each(*iterables: Iterable[_T]) -> List[List[_T]]: ...
@overload
def windowed(
    seq: Iterable[_T], n: int, *, step: int = ...
) -> Iterator[Tuple[Optional[_T], ...]]: ...
@overload
def windowed(
    seq: Iterable[_T], n: int, fillvalue: _U, step: int = ...
) -> Iterator[Tuple[Union[_T, _U], ...]]: ...
def substrings(iterable: Iterable[_T]) -> Iterator[Tuple[_T, ...]]: ...
def substrings_indexes(
    seq: Sequence[_T], reverse: bool = ...
) -> Iterator[Tuple[Sequence[_T], int, int]]: ...

class bucket(Generic[_T, _U], Container[_U]):
    def __init__(
        self,
        iterable: Iterable[_T],
        key: Callable[[_T], _U],
        validator: Optional[Callable[[object], object]] = ...,
    ) -> None: ...
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Iterator[_U]: ...
    def __getitem__(self, value: object) -> Iterator[_T]: ...

def spy(
    iterable: Iterable[_T], n: int = ...
) -> Tuple[List[_T], Iterator[_T]]: ...
def interleave(*iterables: Iterable[_T]) -> Iterator[_T]: ...
def interleave_longest(*iterables: Iterable[_T]) -> Iterator[_T]: ...
def collapse(
    iterable: Iterable[Any],
    base_type: Optional[type] = ...,
    levels: Optional[int] = ...,
) -> Iterator[Any]: ...
@overload
def side_effect(
    func: Callable[[_T], object],
    iterable: Iterable[_T],
    chunk_size: None = ...,
    before: Optional[Callable[[], object]] = ...,
    after: Optional[Callable[[], object]] = ...,
) -> Iterator[_T]: ...
@overload
def side_effect(
    func: Callable[[List[_T]], object],
    iterable: Iterable[_T],
    chunk_size: int,
    before: Optional[Callable[[], object]] = ...,
    after: Optional[Callable[[], object]] = ...,
) -> Iterator[_T]: ...
def sliced(seq: Sequence[_T], n: int) -> Iterator[Sequence[_T]]: ...
def split_at(
    iterable: Iterable[_T],
    pred: Callable[[_T], object],
    maxsplit: int = ...,
    keep_separator: bool = ...,
) -> Iterator[List[_T]]: ...
def split_before(
    iterable: Iterable[_T], pred: Callable[[_T], object], maxsplit: int = ...
) -> Iterator[List[_T]]: ...
def split_after(
    iterable: Iterable[_T], pred: Callable[[_T], object], maxsplit: int = ...
) -> Iterator[List[_T]]: ...
def split_when(
    iterable: Iterable[_T],
    pred: Callable[[_T, _T], object],
    maxsplit: int = ...,
) -> Iterator[List[_T]]: ...
def split_into(
    iterable: Iterable[_T], sizes: Iterable[Optional[int]]
) -> Iterator[List[_T]]: ...
@overload
def padded(
    iterable: Iterable[_T],
    *,
    n: Optional[int] = ...,
    next_multiple: bool = ...
) -> Iterator[Optional[_T]]: ...
@overload
def padded(
    iterable: Iterable[_T],
    fillvalue: _U,
    n: Optional[int] = ...,
    next_multiple: bool = ...,
) -> Iterator[Union[_T, _U]]: ...
@overload
def repeat_last(iterable: Iterable[_T]) -> Iterator[_T]: ...
@overload
def repeat_last(
    iterable: Iterable[_T], default: _U
) -> Iterator[Union[_T, _U]]: ...
def distribute(n: int, iterable: Iterable[_T]) -> List[Iterator[_T]]: ...
@overload
def stagger(
    iterable: Iterable[_T],
    offsets: _SizedIterable[int] = ...,
    longest: bool = ...,
) -> Iterator[Tuple[Optional[_T], ...]]: ...
@overload
def stagger(
    iterable: Iterable[_T],
    offsets: _SizedIterable[int] = ...,
    longest: bool = ...,
    fillvalue: _U = ...,
) -> Iterator[Tuple[Union[_T, _U], ...]]: ...

class UnequalIterablesError(ValueError): ...

def zip_equal(*iterables: Iterable[_T]) -> Iterator[Tuple[_T, ...]]: ...
@overload
def zip_offset(
    *iterables: Iterable[_T], offsets: _SizedIterable[int], longest: bool = ...
) -> Iterator[Tuple[Optional[_T], ...]]: ...
@overload
def zip_offset(
    *iterables: Iterable[_T],
    offsets: _SizedIterable[int],
    longest: bool = ...,
    fillvalue: _U
) -> Iterator[Tuple[Union[_T, _U], ...]]: ...
def sort_together(
    iterables: Iterable[Iterable[_T]],
    key_list: Iterable[int] = ...,
    reverse: bool = ...,
) -> List[Tuple[_T, ...]]: ...
def unzip(iterable: Iterable[Sequence[_T]]) -> Tuple[Iterator[_T], ...]: ...
def divide(n: int, iterable: Iterable[_T]) -> List[Iterator[_T]]: ...
def always_iterable(
    obj: object,
    base_type: Union[
        type, Tuple[Union[type, Tuple[Any, ...]], ...], None
    ] = ...,
) -> Iterator[Any]: ...
def adjacent(
    predicate: Callable[[_T], bool],
    iterable: Iterable[_T],
    distance: int = ...,
) -> Iterator[Tuple[bool, _T]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T], keyfunc: None = ..., valuefunc: None = ...
) -> Iterator[Tuple[_T, Iterator[_T]]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T], keyfunc: Callable[[_T], _U], valuefunc: None = ...
) -> Iterator[Tuple[_U, Iterator[_T]]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: None = ...,
    valuefunc: Callable[[_T], _V] = ...,
) -> Iterator[Tuple[_T, Iterator[_V]]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: Callable[[_T], _V],
) -> Iterator[Tuple[_U, Iterator[_V]]]: ...

class numeric_range(Generic[_T, _U], Sequence[_T], Hashable, Reversible[_T]):
    @overload
    def __init__(self, __stop: _T) -> None: ...
    @overload
    def __init__(self, __start: _T, __stop: _T) -> None: ...
    @overload
    def __init__(self, __start: _T, __stop: _T, __step: _U) -> None: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, elem: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, key: int) -> _T: ...
    @overload
    def __getitem__(self, key: slice) -> numeric_range[_T, _U]: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __len__(self) -> int: ...
    def __reduce__(
        self,
    ) -> Tuple[Type[numeric_range[_T, _U]], Tuple[_T, _T, _U]]: ...
    def __repr__(self) -> str: ...
    def __reversed__(self) -> Iterator[_T]: ...
    def count(self, value: _T) -> int: ...
    def index(self, value: _T) -> int: ...  # type: ignore

def count_cycle(
    iterable: Iterable[_T], n: Optional[int] = ...
) -> Iterable[Tuple[int, _T]]: ...
def locate(
    iterable: Iterable[object],
    pred: Callable[..., Any] = ...,
    window_size: Optional[int] = ...,
) -> Iterator[int]: ...
def lstrip(
    iterable: Iterable[_T], pred: Callable[[_T], object]
) -> Iterator[_T]: ...
def rstrip(
    iterable: Iterable[_T], pred: Callable[[_T], object]
) -> Iterator[_T]: ...
def strip(
    iterable: Iterable[_T], pred: Callable[[_T], object]
) -> Iterator[_T]: ...

class islice_extended(Generic[_T], Iterator[_T]):
    def __init__(
        self, iterable: Iterable[_T], *args: Optional[int]
    ) -> None: ...
    def __iter__(self) -> islice_extended[_T]: ...
    def __next__(self) -> _T: ...
    def __getitem__(self, index: slice) -> islice_extended[_T]: ...

def always_reversible(iterable: Iterable[_T]) -> Iterator[_T]: ...
def consecutive_groups(
    iterable: Iterable[_T], ordering: Callable[[_T], int] = ...
) -> Iterator[Iterator[_T]]: ...
@overload
def difference(
    iterable: Iterable[_T],
    func: Callable[[_T, _T], _U] = ...,
    *,
    initial: None = ...
) -> Iterator[Union[_T, _U]]: ...
@overload
def difference(
    iterable: Iterable[_T], func: Callable[[_T, _T], _U] = ..., *, initial: _U
) -> Iterator[_U]: ...

class SequenceView(Generic[_T], Sequence[_T]):
    def __init__(self, target: Sequence[_T]) -> None: ...
    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[_T]: ...
    def __len__(self) -> int: ...

class seekable(Generic[_T], Iterator[_T]):
    def __init__(
        self, iterable: Iterable[_T], maxlen: Optional[int] = ...
    ) -> None: ...
    def __iter__(self) -> seekable[_T]: ...
    def __next__(self) -> _T: ...
    def elements(self) -> SequenceView[_T]: ...
    def seek(self, index: int) -> None: ...

class run_length:
    @staticmethod
    def encode(iterable: Iterable[_T]) -> Iterator[Tuple[_T, int]]: ...
    @staticmethod
    def decode(iterable: Iterable[Tuple[_T, int]]) -> Iterator[_T]: ...

def exactly_n(
    iterable: Iterable[_T], n: int, predicate: Callable[[_T], object] = ...
) -> bool: ...
def circular_shifts(iterable: Iterable[_T]) -> List[Tuple[_T, ...]]: ...
def make_decorator(
    wrapping_func: Callable[..., _U], result_index: int = ...
) -> Callable[..., Callable[[Callable[..., Any]], Callable[..., _U]]]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: None = ...,
    reducefunc: None = ...,
) -> Dict[_U, List[_T]]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: Callable[[_T], _V],
    reducefunc: None = ...,
) -> Dict[_U, List[_V]]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: None = ...,
    reducefunc: Callable[[List[_T]], _W] = ...,
) -> Dict[_U, _W]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: Callable[[_T], _V],
    reducefunc: Callable[[List[_V]], _W],
) -> Dict[_U, _W]: ...
def rlocate(
    iterable: Iterable[_T],
    pred: Callable[..., object] = ...,
    window_size: Optional[int] = ...,
) -> Iterator[int]: ...
def replace(
    iterable: Iterable[_T],
    pred: Callable[..., object],
    substitutes: Iterable[_U],
    count: Optional[int] = ...,
    window_size: int = ...,
) -> Iterator[Union[_T, _U]]: ...
def partitions(iterable: Iterable[_T]) -> Iterator[List[List[_T]]]: ...
def set_partitions(
    iterable: Iterable[_T], k: Optional[int] = ...
) -> Iterator[List[List[_T]]]: ...
def time_limited(
    limit_seconds: float, iterable: Iterable[_T]
) -> Iterator[_T]: ...
@overload
def only(
    iterable: Iterable[_T], *, too_long: Optional[_Raisable] = ...
) -> Optional[_T]: ...
@overload
def only(
    iterable: Iterable[_T], default: _U, too_long: Optional[_Raisable] = ...
) -> Union[_T, _U]: ...
def ichunked(iterable: Iterable[_T], n: int) -> Iterator[Iterator[_T]]: ...
def distinct_combinations(
    iterable: Iterable[_T], r: int
) -> Iterator[Tuple[_T, ...]]: ...
def filter_except(
    validator: Callable[[Any], object],
    iterable: Iterable[_T],
    *exceptions: Type[BaseException]
) -> Iterator[_T]: ...
def map_except(
    function: Callable[[Any], _U],
    iterable: Iterable[_T],
    *exceptions: Type[BaseException]
) -> Iterator[_U]: ...
def sample(
    iterable: Iterable[_T], k: int, weights: Optional[Iterable[float]] = ...,
) -> List[_T]: ...
