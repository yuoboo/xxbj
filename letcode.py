# encoding=utf8
import time


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    _result = list()
    _len = len(nums)
    i = 0
    while i < _len:
        num_1 = nums[i]
        num_2 = target - num_1
        j = i + 1
        while j < _len:
            if num_2 == nums[j]:
                _result = [i, j]
            j += 1
        i += 1
    return _result


# 两个数之和
def twonums(nums, target):
    d = dict()
    for i,value in enumerate(nums):
        tmp = target - value
        if tmp in d:
            return [d[tmp], i]

        d[value] = i
    return []


# 最长字符串
def stringlenght(s):
    '''
    返回最长不重复字符串的长度: abcabcdabc --> 4 abbcd
    :param s:  思路: 滑动视窗
    :return:
    '''
    max_len = 0
    num = 0
    tmp = ''
    for i in s:
        if i not in tmp:
            tmp += i
            num += 1
        else:
            index_i = tmp.index(i)
            tmp = tmp[index_i+1:]+i
            num = len(tmp)

        if num > max_len:
            max_len = num

    return max_len


# 数字反转
def num_reverse(x):
    _p = pow(2, 31)
    _min = - _p
    _max = _p - 1
    flag = True
    if x < 0:
        flag = False
    _list = list(str(abs(x)))
    _list.reverse()
    _num = int(''.join(_list))
    if not flag:
        _num = - _num

    if _num < _min or _num > _max:
        _num = 0
    return _num


# 将字符串转为整数
def str2num(s):
    _min = 0 - pow(2, 31)
    _max = pow(2, 31) - 1
    _res = 0
    _s = s.strip()
    if not _s:
        return _res

    if _s[0] not in '0123456789-+':
        return _res

    tmp = ''
    for i in _s[1:]:
        if i in "0123456789":
            tmp += i
        else:
            break

    if _s[0] in '-+':
        if len(tmp) == 0:
            return _res

    _res = int(_s[0] + tmp)
    if _res < _min:
        return _min
    elif _res > _max:
        return _max
    else:
        return _res


# 回文数判断
def isPalindrome(x):
    if x < 0:
        return False

    _res = str(x)[::-1]
    if int(_res) == x:
        return True
    return False


def _fn(x, y):
    _res = ''
    if not x or not y:
        return _res

    if len(x) > len(y):
        for i,v in enumerate(y):
            if v == x[i]:
                _res += v
            else:
                break
    else:
        for i,v in enumerate(x):
            if v == y[i]:
                _res += v
            else:
                break
    return _res


# 最长公共前缀
def longestCommonPrefix(strs):
    if not strs:
        return ''

    return reduce(_fn, strs)


def test_long(strs):
    if len(strs) == 0:
        return ""

    _pre = strs[0]

    for i in range(len(strs)):

        if _pre == "":
            return _pre

        while strs[i].find(_pre) != 0:
            _pre = _pre[:len(_pre) - 1]

    return _pre


# 三数之和 a+b+c=0
def threeSum(nums):
    nums = [-1, 0, 1, 2, -1, -4]
    num_1 = []
    num_2 = []
    for i in nums:
        if i > 0:
            num_2.append(i)
        else:
            num_1.append(i)
    for i,v in enumerate(num_1):
        pass

    pass


if __name__ == '__main__':

    # a = twoSum([2,2], 4)
    # print a
    #
    # a = twoSum([2,3,4], 4)
    # print a

    # a = twonums([3, 3], 6)
    # print a

    # s = stringlenght("abbcddddecabfg")
    # print s

    # print num_reverse(-123)
    # print num_reverse(-12345678911)
    # print num_reverse(1223423456774)
    # print num_reverse(122324456)

    # print str2num('   -42')
    # print str2num('-42df345 wff 555')
    # print str2num('4193 with words')
    # print str2num('-91283472332')
    # print str2num('+')
    # print str2num('')
    # print str2num('+1123-3333')
    # print str2num('-133vvv')
    # print str2num('-+1233')

    # print isPalindrome(121)
    # print isPalindrome(-121)
    # print isPalindrome(+10)

    # print longestCommonPrefix(['', '12'])
    # print longestCommonPrefix([])
    # print longestCommonPrefix(['11', '12', '1fgg'])
    # print longestCommonPrefix(['abcd11', 'abc12', '1cdfgg'])
    # print longestCommonPrefix(['add', '12', '1fgg'])
    # print longestCommonPrefix(["flower","flow","flight"])
    # print longestCommonPrefix([''])

    print test_long([''])
    print test_long([])
    print test_long(['', '12'])
    print test_long(["flower", "flow", "flight"])
    print test_long(['11', '12', '1fgg'])

