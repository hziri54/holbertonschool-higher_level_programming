#!/usr/bin/python3
"""Task 3: Counted Iterator"""


class CountedIterator:
    """Counted Iterator"""

    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            a = next(self.iterator)
            self.counter += 1
            return a
        except StopIteration:
            raise StopIteration
