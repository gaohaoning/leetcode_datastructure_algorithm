#!/usr/bin/env python
# coding:utf-8

"""
167. 两数之和 II - 输入有序数组
难度
简单

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


# ================================================================================
# ================================================================================
"""
思路1:
二分查找: 先确定一个数，再用二分查找搜索另一个数

时间复杂度:
    O(nlogn)
"""
"""
这个超出时间限制了 !!!!!
"""
class Solution(object):
    def binary_search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # left = mid  # !!!!!
                left = mid + 1
            elif nums[mid] > target:
                # right = mid  # !!!!!
                right = mid - 1
            pass
        return -1
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            ns = numbers[i + 1:]
            pos = self.binary_search(ns, target - numbers[i])
            if pos != -1:
                return i + 1, i + 1 + pos + 1
# ================================================================================
"""
思路2：
指针对撞法
    利用两个指针分别指向头尾，通过头尾数之和和目标数进行比较，前者大则尾指针左移，前者小则指针右移。
    充分利用了排好序数组这一特性。

时间复杂度:
    O(n)
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
        return left + 1, right + 1
# ================================================================================

