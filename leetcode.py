# encoding=utf8
def _removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    value_i = None
    for j, v in enumerate(nums):
        if v != value_i:
            i += 1
            value_i = v

    return i


# 字符组合
def _letterCombinations(digits):

    _d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return 0

    _init = [_d[i] for i in digits]

    _res = list(_init[0])
    for _v in _init[1:]:
        _tmp = []
        for _j in _v:
            _tmp += list(map(lambda x: x + _j, _res))
        _res = _tmp
    _res.sort()
    return _res


# 实现for循环
def test_for(param):
    if isinstance(param, (str, list, tuple, dict)):
        _tmp = iter(param)
        try:
            while True:
                # print next(_tmp),
                print _tmp.next(),
        except StopIteration as e:
            print ''
    else:
        print '参数不可遍历'


# 实现位移除法
def divide(dividend, divisor):
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    # 判断是否同号
    sign = abs(dividend + divisor) > max(abs(dividend), abs(divisor))
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0

    if divisor == 0:
        return None

    # 统计减法次数i, 位移因子n, 左移一次n增加16倍
    while (dividend >= divisor):
        tmp, i = divisor, 1
        n = 4
        while (dividend >= tmp):
            dividend -= tmp
            res += i

            tmp = tmp << n
            i = i << n

    if not sign:
        res = -res

    if INT_MIN <= res < INT_MAX:  # 判断结果是否溢出
        return res
    else:
        return INT_MAX


if __name__ == '__main__':
    # _nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # print _removeDuplicates(_nums)
    #
    # print _letterCombinations('')
    # print _letterCombinations('23')
    # print _letterCombinations('567')

    # test_for('12345')
    # test_for({"a": 1, "b": 2, "c": 3})

    print divide(10, 0)
    print divide(-7, 2)
    print divide(10000, -3)
    print divide(-9, -10)
