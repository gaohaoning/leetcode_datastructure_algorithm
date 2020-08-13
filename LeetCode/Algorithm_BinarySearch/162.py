#!/usr/bin/env python
# coding:utf-8

"""
162. 寻找峰值
难度
中等

峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。
"""


# ================================================================================
"""
时间复杂度不达标 !!!

方法1: 线性搜索（只需要找到第一个 nums[i] > nums[i+1] 的 i 即可）
    Time complexity : O(n)
    Space complexity : O(1)
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        # 考虑到 nums[-1] = nums[n] = -∞ ，首先判断首尾元素是否是峰值.
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        #
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

# ================================================================================
"""
方法2: 二分查找
思路: 使用二分法:
    若 mid > mid+1 则 0 ~ mid 必然有一个peak
    若 mid < mid+1 则 mid ~ len(nums) 必然一个peak

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        # 考虑到 nums[-1] = nums[n] = -∞ ，首先判断首尾元素是否是峰值.
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        # 除去首尾元素后，二分查找 !!!!!
        left, right = 1, len(nums) - 2
        while left <= right:
            mid = (left + right)/2
            if mid == right:
                # 避免陷入无限循环 !!!
                break
            if nums[mid] > nums[mid + 1]:
                right = mid
                pass
            else:
                left = mid + 1
                pass
            pass
        return right

# ================================================================================
"""
(方法2 的另一种写法)
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        # 考虑到 nums[-1] = nums[n] = -∞ ，首先判断首尾元素是否是峰值.
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        # 除去首尾元素后，二分查找 !!!!!
        left, right = 1, len(nums) - 2
        while left < right:
            # 注意: 循环条件不能用 left <= right，那样会陷入无限循环
            mid = (left + right)/2
            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # 遇到 mid 和 mid + 1 相等时移动下 left 或者 right，直至出现不同的值为止
                left += 1
        return right
# ================================================================================
# ================================================================================

