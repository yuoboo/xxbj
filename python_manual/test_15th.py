# encoding=utf8
import random

TEST_VALUE = 100


class TestDoc(object):
    """
    this is doc
    放在模块,函数以及类语句的顶端的字符串,python会自动封装这个字符串,成为文档字符串,
    使其成为相应对象的__doc__属性
    """

    def __init__(self, name):
        self.name = name

    def readbook(self):
        """
        this is readbook __doc__
        """
        print 'this is readbook'


def test_doc():
    '''
    this is doc test
    '''
    print 'this is test doc'


def practice():
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 5

    found = False
    i = 0
    while not found and i < len(L):
        if 2**X == L[i]:
            found = True
        else:
            i += 1
    if found:
        print 'x index %d' %i
    else:
        print 'not found'


def practice_else():
    """
    使用 else 消除 found 标志位
    """
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 50
    i = 0
    while i < len(L):
        if 2**X == L[i]:
            print 'x index %d' % i
            break
        i += 1
    else:
        print 'not found'


def practice_for():
    """
    for循环消除 计数因子 i
    """
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 50

    for i in L:
        if 2**X == i:
            print 'x index %d' % L.index(i)
            break
    else:
        print 'not found'


def practice_in():
    """
    使用 in 成员关系测试 消除循环
    """
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 50

    if 2**X in L:
        print 'x index %d' % L.index(2**X)
    else:
        print 'not found'


if __name__ == '__main__':

    # 测试__doc__
    # t = TestDoc("test")
    # print t.__doc__
    # print t.readbook.__doc__

    # print test_doc.__doc__

    # print help(TestDoc)
    practice()
    practice_for()
    practice_in()
