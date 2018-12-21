# encoding=utf8
'''
斐波拉契数列
'''


# 1,1,2,3,5,8,13....


def fib(n):
    a = 0
    b = 1
    while b <= n:
        print b
        a, b = b, a + b


# fib(100)


def _fib(n):
    a = 0
    b = 1
    count = 1
    while count <= n:
        # print b
        a, b = b, a + b
        count += 1
    print b

# _fib(50)


def foo(n):
    count = 0
    while count < n:
        yield count
        count += 1
    # return "done"    python<3.3 生成器中不允许return 后面跟参数的写法


# for i in foo(5):
#     print(i)


# [1,2,4,3,7,30,22,8]  找出数组中左边都比它小 右边都比它的大的数  [1,2,7]满足
# 思路:
# 使用一个数组nArrMin[i]来保存[i,nLen-1]区间内的最小值。
# 使用一个变量nMax保存区间[0,i-1]的最大值。
# 对于第i个数，如果它满足nArr[i]大于左边的最大数nMax 且 小于右边的最小数nArrMin[i]，则该数即为所求


def test_list(l):
    _len = len(l)
    i = 0
    right_min = [None] * (_len - 1)
    right_min.append(l[-1])

    # 反向遍历
    while i < _len:
        _count = _len - 1 - i
        if i == _len - 1:
            break
        if l[_count] <= right_min[_count]:
            right_min[_count - 1] = l[_count]
        else:
            right_min[_count - 1] = right_min[_count]

        i += 1

    print right_min
    # 正向遍历
    _n = 0
    res = list()
    left_max = l[0]
    while _n < _len:
        if _n == 0:
            if l[0] < right_min[0]:
                res.append(l[0])
        elif _n == _len - 1:
            if l[_n] > left_max:
                res.append(l[_n])
        else:
            if l[_n] > left_max:
                left_max = l[_n]
                if l[_n] < right_min[_n]:
                    res.append(l[_n])
        _n += 1

    print res


# n个台阶, 一次走1个或者2个, 有多少种走法
# 如果总共有f(n)中走法, 第一次走1步,剩余可以走f(n-1)种, 第一步走2个剩余有f(n-2)种走法
# f(n) = f(n-1)+f(n-2)  斐波拉契数列的第N列

def _louti(n):
    a = 0
    b = 1
    count = 1
    while count <= n:
        a, b = b, a+b
        count += 1
    print b


if __name__ == '__main__':
    l = [1, 2, 4, 3, 7, 30, 22, 8, 40, 43, 44, 70, 45, 70]
    # test_list(l)

    # _louti(3)
    # _louti(5)
    # _louti(50)

    f = foo(5)
    while 1:
        try:
            print next(f)
        except StopIteration as e:
            break

    import sys
    print sys.path