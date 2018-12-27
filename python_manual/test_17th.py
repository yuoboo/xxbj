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


# 状态保持一般使用类存储比较规则, 但是使用def嵌套其实更简单
class Tester(object):
    def __init__(self, start):
        self.state = start

    def nested(self, label):
        print(label, self.state)
        self.state += 1


class Testero(object):
    def __init__(self, start):
        self.state = start

    def __call__(self, label):
        print(label, self.state)
        self.state += 1


def tester(start):
    state = start

    def nested(label):
        nonlocal state  # python3
        print(label, state)
        state += 1
    return nested


def funcer(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1

    nested.state = start
    return nested


def func(x=0, y=[]):
    print(y)
    y.append(x)
    print(y)


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

    # test_non()

    # f = funcer(1)
    # f('f1')
    # g = funcer(1)
    # g('g1')
    # g('g2')
    # g('g3')
    # f('f2')
    # f('f3')

    func()  # [0]
    func(1, [1])  # [1,1]
    func(1)  # [0, 1]
    func(2)
    func(3, [])
    func(4)
    func()
