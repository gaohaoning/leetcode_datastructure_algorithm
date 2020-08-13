#!/usr/bin/env python
# coding:utf-8

"""
219. 存在重复元素 II

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""


# ================================================================================
# ================================================================================
"""
思路:
    先判断相等，再计算距离
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        used = {}
        for i, n in enumerate(nums):
            if n not in used:
                used[n] = i
            else:
                distance = i - used[n]
                if distance <= k:
                    return True
                used[n] = i
                pass
            pass
        return False

# ================================================================================
# ================================================================================
so = Solution()
# print so.containsNearbyDuplicate([1,2,3,1,2,3], 2)
print so.containsNearbyDuplicate([99, 99], 2)
# ================================================================================
# ================================================================================

