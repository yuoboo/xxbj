# encoding=utf8

# 没有限制范围的分片表达式能够复制序列
l = [1, 2, 3]
l1 = l[:]
l[0] = 0
print l, l1

# 字典的copy方法可以复制字典
d = {'a': 1, 'b': 2}
d1 = d.copy()
d['a'] = 11
print d, d1


# 有些内置函数能够生成拷贝(list)
l2 = list(l)
l[0] = 11
print l, l1, l2

# copy标准库也能拷贝
# 以上4中拷贝均为顶层拷贝, 如果有嵌套存在需要使用深度拷贝

ll = {'a': [1,2,3], 'b': 11, 'c': ['aa', 'bb', {"_a": '_a'}]}
ll1 = ll.copy()

ll['a'][1] = 22
# copy.deepcopy()  深拷贝

import copy

ll2 = copy.deepcopy(ll)
ll['c'][1] = 0
print ll
print ll1
print ll2


