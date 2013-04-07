from itertools import zip_longest

def chunked_alternate(iterable, size, strict=False):
    """Like current chunked(), but probably faster and with optional error-handling.

    Default behavior is like chunked (well, returning tuples instead of lists.
    With strict = True, however, raises ValueError if iterable is not evenly divisible by size."""

    fillvalue = object()
    args = [iter(iterable)]*size
    chunks = zip_longest(*args, fillvalue=fillvalue)
    prev = next(chunks)

    for chunk in chunks:
        yield prev
        prev = chunk

    if prev[-1] is fillvalue:
        while prev[-1] is fillvalue:
            prev = prev[:-1]

        if strict:
            raise ValueError("only %d value(s) left in iterator, expected %d" % (len(prev),size))

    yield prev
