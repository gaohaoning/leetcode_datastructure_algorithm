#!/usr/bin/env python
# coding:utf-8

"""
Python 笔记
"""

# ================================================================================
"""
列表切片可以放在"="左边，用作列表元素的赋值
"""
l = range(9)
print l
l[1:4] = [11, 22, 33]
print l
# ================================================================================
"""
a = b = c = 1
的实际执行顺序是:
a=1, b=a, c=a
"""
l = []
x = 9
l[len(l):] = [x]
print l
# [9]

l = []
x = 9
l[len(l):] = l[len(l):] = [x]
print l
# [9, 9]

l = []
x = 9
l = l[len(l):] = l[len(l):] = [x]
print l
# [9, 9, 9, 9]

l = []
x = 9
# l = l[len(l):] = l[len(l):] = [x]
l = [x]
l[len(l):] = l
l[len(l):] = l
print l
# [9, 9, 9, 9]
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
