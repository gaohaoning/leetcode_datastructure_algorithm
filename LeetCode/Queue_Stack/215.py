#!/usr/bin/env python
# coding:utf-8

"""
215. 数组中的第K个最大元素
难度
中等

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
# ================================================================================
"""
思路:
    使用 优先队列（heapq）
时间复杂度:
    大小为 k 的堆中添加元素的时间复杂度为 O(logk)
    O(n * logk)
空间复杂度: 
    O(k)
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums):
            return False
        import heapq
        hq = nums[:k]
        heapq.heapify(hq)
        for i in range(k, len(nums)):
            heapq.heappushpop(hq, nums[i])
            pass
        return hq[0]


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k, nums)[-1]

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

so = Solution()
print so.findKthLargest(4, [3,2,3,1,2,4,5,5,6])

