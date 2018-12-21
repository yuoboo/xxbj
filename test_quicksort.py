def quick_sort(l, start=0, end=None):
    if end is None:
        end = len(l) - 1

    _tmp = l[start]
    _left = start
    _right = end

    if start >= end:
        return

    while _left < _right:
        while l[_right] >= _tmp and _left < _right:
            _right -= 1

        l[_left] = l[_right]

        while l[_left] < _tmp and _left < _right:
            _left += 1

        l[_right] = l[_left]

    l[_left] = _tmp

    quick_sort(l, start, _left - 1)
    quick_sort(l, _left + 1, end)


if __name__ == '__main__':
    l = [11, 33, 77, 44, 3333, 55, 66, 99, 77, 33, 22, 11, 444444]
    quick_sort(l, 1, 6)
    quick_sort(l)
    print l


def quick_sort(l, start, end):

    if start >= end:
        return

    _tmp = l[0]
    _left = start
    _right = end

    while _left < _right:
        while _left < _right and l[_right] >= _tmp:
            _right -= 1

        l[_left] = l[_right]

        while _left < _right and l[_left] < _tmp:
            _left += 1

        l[_right] = l[_left]

    l[_left] = _tmp
    
    quick_sort(l, start, _left-1)
    quick_sort(l, _left+1, end)


if __name__ == '__main__':
    l = [11, 22, 55, 66, 777, 8, 33, 22, 99, 1, 22, 77, 444, 33, 222, 77]
    quick_sort(l)
