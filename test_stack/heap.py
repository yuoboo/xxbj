# encoding = utf8
from heapq import heappush, heappop, heapify


def _stack():
    a = 1
    b = 2
    print id(a)
    print id(b)


def _heap():
    heap = []
    heappush(heap, 2)
    heappush(heap, 'aaaa')
    print heap
    i = heappop(heap)
    a = heappop(heap)
    print i, id(i)
    print a, id(a)


if __name__ == '__main__':
    _stack()
    _heap()
