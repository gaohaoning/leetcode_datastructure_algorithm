#!/usr/bin/env python
# coding:utf-8

"""
34. 在排序数组中查找元素的第一个和最后一个位置
难度
中等

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


# ================================================================================
"""
（不推荐）
方法1:
投机取巧，利用 python 的现成函数
"""
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         l = []
#         while True:
#             try:
#                 l.append(nums.index(target, l[-1] + 1 if l else 0))
#             except Exception, e:
#                 break
#
#         return (l[0], l[-1]) if l else (-1, -1)

# ================================================================================
"""
解法: 
    二分查找
思路:
    先用二分查找找到一个位置，再向两侧延伸到边界。
时间复杂度: 
    O(log n)
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # nums[mid] == target
                left, right = mid, mid
                while left >= 0 and nums[left] == nums[mid]:
                    left -= 1
                while right <= len(nums) - 1 and nums[right] == nums[mid]:
                    right += 1
                return [left + 1, right - 1]
                pass
            pass

        return [-1, -1]
# ================================================================================
# ================================================================================

nums = [5,7,7,8,8,10]
target = 8
so = Solution()
print so.searchRange(nums, target)
# (3, 4)
