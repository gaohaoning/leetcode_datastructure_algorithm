#!/usr/bin/env python
# coding:utf-8

"""
集合操作
    s.intersection(t) 	        s & t 	new set with elements common to s and t
    s.union(t) 	                s | t 	new set with elements from both s and t
    s.difference(t) 	        s - t 	new set with elements in s but not in t
    s.symmetric_difference(t) 	s ^ t 	new set with elements in either s or t but not both
"""
# ================================================================================
import random
s1 = set([random.randint(0, 100) for _ in range(100)])
s2 = set([random.randint(0, 100) for _ in range(100)])

print s1
print s2

# ================================================================================
"""
交集
"""
print s1.intersection(s2)
print s1 & s2

"""
并集
"""
print s1.union(s2)
print s1 | s2

"""
差集
"""
print s1.difference(s2)
print s1 - s2

"""
对称差集
"""
print s1.symmetric_difference(s2)
print s1 ^ s2

# ================================================================================
# ================================================================================



