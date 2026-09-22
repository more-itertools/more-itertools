import platform
import unittest

from more_itertools import seekable


class SeekableMemoryTests(unittest.TestCase):
    @unittest.skipUnless(
        platform.python_implementation() == 'CPython',
        'retained allocation check uses CPython tracemalloc',
    )
    def test_repeated_zero_cache_peek_has_bounded_memory(self):
        import tracemalloc

        if tracemalloc.is_tracing():
            self.skipTest('do not disturb an existing allocation trace')
        iterator = seekable(range(3), maxlen=0)
        tracemalloc.start()
        try:
            iterator.peek()
            baseline = tracemalloc.get_traced_memory()[0]
            for _ in range(10000):
                iterator.peek()
                bool(iterator)
            retained = tracemalloc.get_traced_memory()[0] - baseline
        finally:
            tracemalloc.stop()
        # A lookahead needs one item, not one iterator per peek/truth test.
        self.assertLess(retained, 256 * 1024)
        self.assertEqual(list(iterator.elements()), [])
        self.assertEqual(list(iterator), [0, 1, 2])
