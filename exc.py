from __future__ import print_function
from more_itertools import consume, side_effect

def iterable():
    yield 1
    raise RuntimeError('uh oh')
    yield 2

class Manager(object):
    def __enter__(self):
        print('Enter')
        return self

    def __exit__(self, *args, **kwargs):
        print('Exit')


manager = Manager()
it = iterable()
try:
    consume(print(x) for m in context(manager) for x in it)
except RuntimeError:
    print('Encountered exception!')
