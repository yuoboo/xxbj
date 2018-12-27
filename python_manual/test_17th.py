#encoding=utf8

import time
import random
from functools import wraps
# import test_15th

# print test_15th.TEST_VALUE
# test_15th.TEST_VALUE = 10



CACHE = dict()
def _cache(n):
    def decorator(func):
        @wraps(func)
        def _wrapper(keywords):
            _now = time.time()
            if keywords in CACHE and (_now - CACHE[keywords][1] < n):
                return CACHE[keywords][0]
            CACHE[keywords] = (func(keywords), _now)
            return CACHE[keywords][0]
        return _wrapper
    return decorator


def get_value(key):
    # print key,
    return random.random()


@_cache(2)
def func_test(key):
    new = get_value(key)
    return new


def test_nonlocal(func):
    x = 99
    print('x:', x)

    @wraps(func)
    def _wrapper(x=x):
        print('x:', x)
        x = 100
        print('x:', x)
        return func()

    return _wrapper


@test_nonlocal
def test_non():
    print('this is non')





if __name__ == '__main__':
    # print func_test(1)
    # print func_test(2)
    # print func_test(1)
    # time.sleep(3)
    # print func_test(2)
    # print func_test(2)
    # print func_test(1)
    # time.sleep(3)
    # print func_test(1)

    test_non()