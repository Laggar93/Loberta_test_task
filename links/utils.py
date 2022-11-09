import itertools


def chunk(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))

    while item:
        yield item
        item = list(itertools.islice(it, size))