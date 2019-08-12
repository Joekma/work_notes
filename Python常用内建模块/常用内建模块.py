# coding:utf-8

import itertools

'''Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数'''


# count(start=0, step=1)  创建一个无限迭代器
# natuals = itertools.count(2)
# for i in natuals:
#     print i


# cycle(iterable) 无限循环一个可迭代的序列
# itertools.cycle()

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# ns = itertools.repeat('A', 10)
# for n in ns:
#     print n

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# for n in ns:
#     print n

# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
#
# for c in itertools.chain('ABC', 'XYZ'):
#     print c
# # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

#groupby()

# groupby()把迭代器中相邻的重复元素挑出来放在一起

# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print key, list(group) # 为什么这里要用list()函数呢？

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：

# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#    print key, list(group)

# imap()
# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。

# for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
#     print x

# 注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕

# r = map(lambda x: x*x, [1, 2, 3])
# r # r已经计算出来了
# 当你调用imap()时，并没有进行任何计算