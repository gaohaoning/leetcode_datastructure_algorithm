#!/usr/bin/env python
# coding:utf-8

"""
169. 求众数

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""


# ================================================================================
"""
普通方法: 循环计数

Time complexity : O(n)
Space complexity : O(n)
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        return max(c.keys(), key=c.get)
# ================================================================================
"""
分治法(没有完全理解) ?????????????????????????????????????????????

Time complexity : O(nlgn)
Space complexity : O(lgn)
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def major(a, b):
            if a == b:
                return nums[a]
            mid = a + (b - a)//2
            left = major(a, mid)  # 递归
            right = major(mid + 1, b)  # 递归
            #
            if left == right:
                return left
            #
            left_count = sum(1 for i in range(a, b + 1) if nums[i] == left)
            right_count = sum(1 for i in range(a, b + 1) if nums[i] == right)
            return left if left_count > right_count else right
        return major(0, len(nums) - 1)

# ================================================================================
# ================================================================================

