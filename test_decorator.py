# encoding=utf8
from functools import wraps

def decorator(func):
    def _wrapper(*args, **kwargs):
        print "this is decotor"
        return func(*args, **kwargs)

    return _wrapper


@decorator
def hello(x, y):
    print 'this is hello'
    print x + y


import time
import random

# _words = None
# _time = 0
_cache = {}  # _cache = {"key": ["value", "_time"]}


def cache(n):
    def decorator(func):
        @wraps(func)
        def _wrapper(keywords):
            global _cache
            _now = time.time()
            if keywords in _cache.keys() and _now - _cache[keywords][-1] < n:
                pass
            else:
                _l = list()
                _l.append(func(keywords))
                _l.append(_now)
                _cache[keywords] = _l

            return _cache[keywords][0]

        return _wrapper

    return decorator


@cache(3)
def query(keywords):
    print "keywords", keywords
    return random.random()


# 类装饰器
class Decorator(object):
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)


@Decorator
def test_func(x, y):
    print 'this is test_func'
    return x+y


class _Cache(object):

    def __init__(self, func):
        print 'this is init'
        self.__func = func

    def __call__(self, *args, **kwargs):
        print "this is call"
        res = self.__func(*args)
        return res


@_Cache
def _Cache_test(x, y):
    print "this is test"
    return x+y


if __name__ == '__main__':
    # @decorator 将decorator下面的函数当做参数传递给decorator函数并执行赋值给原函数变量 hello = decorator(hello)
    # 此时hello指向了_wrapper函数  func 接收了 hello原函数对象, 由于_wrapper被引用 变量func不会被释放
    # 调用hello() 相当于调用 _wrapper(),

    # hello(1, 2)
    # a = hello.__name__
    # print a

    # print query(1)
    # time.sleep(2)
    # print query(1)
    # time.sleep(2)
    # print query(2)
    # print query(1)
    # print query(3)
    # print query(2)
    # print _cache

    # ===================
    # print test_func(1, 2)
    print _Cache_test(1,2)