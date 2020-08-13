#!/usr/bin/env python
# coding:utf-8

"""
350. 两个数组的交集 II

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


# ================================================================================
# 方法1 (代码较麻烦)
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = {}
        s2 = {}
        sret = {}
        for n in nums1:
            s1[n] = s1.get(n, 0) + 1
            pass
        for n in nums2:
            s2[n] = s2.get(n, 0) + 1
            pass
        for k, v in s1.iteritems():
            if k in s2:
                sret[k] = min(v, s2[k])
                pass
            pass
        ret = []
        for k, v in sret.iteritems():
            ret.extend([k] * v)
            pass
        return ret


# ================================================================================
# 方法2（代码较简洁）
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums1) & set(nums2)
        l = []
        for x in s:
            l.extend([x] * min(nums1.count(x), nums2.count(x)))
            pass
        return l
# ================================================================================
# ================================================================================

