#!/usr/bin/env python
# coding:utf-8

"""
4. 寻找两个有序数组的中位数
难度
困难

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""


# ================================================================================
"""
笨方法(不推荐，不满足时间复杂度要求)：
    合并之后排序。

时间复杂度:
    O(n * logn)
"""
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         nums = nums1 + nums2
#         nums.sort()
#         l = len(nums)
#         return nums[l/2] if l % 2 else (nums[l/2 - 1] + nums[l/2])/2.0

# ================================================================================
"""
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

# ================================================================================
# ================================================================================

