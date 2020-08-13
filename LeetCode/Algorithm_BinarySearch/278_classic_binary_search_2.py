#!/usr/bin/env python
# coding:utf-8

"""
278. 第一个错误的版本
难度
简单

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。
"""


# ================================================================================
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    # l = [0] * 55 + [1] * 45
    l = [1, 1]
    return not not l[version - 1]


"""
关键属性
    一种实现二分查找的高级方法。
    查找条件需要访问元素的直接右邻居。
    使用元素的右邻居来确定是否满足条件，并决定是向左还是向右。
    保证查找空间在每一步中至少有 2 个元素。
    需要进行后处理。 当你剩下 1 个元素时，循环 / 递归结束。 需要评估剩余元素是否符合条件。
"""
"""
二分查找的高级模板。它用于查找需要访问数组中当前索引及其直接右邻居索引的元素或条件。
    Time complexity : O(logn)
    Space complexity : O(1)
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                if mid == 1:
                    return 1
                elif not isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid + 1
                pass

# ================================================================================
# ================================================================================


so = Solution()
print so.firstBadVersion(2)
