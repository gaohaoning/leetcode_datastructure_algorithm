#!/usr/bin/env python
# coding:utf-8

"""
719. 找出第 k 小的距离对
难度
困难

给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

示例 1:

输入：
nums = [1,3,1]
k = 1
输出：0
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
提示:

2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""


# ================================================================================
"""
方法1：
    维护一个小顶堆

时间复杂度(超出时间限制):
    N^2 * logN^2 = N**2 * logN
空间复杂度:
    O(N)
"""
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []  # This is RIGHT
        # heap = heapq.heapify([])  # This is WRONG
        #
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                heapq.heappush(heap, abs(nums[i] - nums[j]))
                pass
            pass
        # print heap
        # [1]
        # for _ in range(k - 1):
        #     heapq.heappop(heap)
        #     pass
        # return heapq.heappop(heap)
        # [2]
        # print heapq.nsmallest(k, heap)
        #
        return heapq.nsmallest(k, heap)[-1]

# ================================================================================
"""
方法2:
    二分查找 + 滑动窗口
时间复杂度:
    O(NlogW + NlogN)
    where N is the length of nums, and W is equal to nums[nums.length - 1] - nums[0]. 
    The logW factor comes from our binary search, and we do O(N) work inside our call to possible (or to calculate count in Java). 
    The final O(NlogN) factor comes from sorting.
空间复杂度:
    O(1)
"""


# TODO: 尚未完全理解 ??????


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        def count_distance_less_than(distance):
            """求距离小于等于 guess - nums[0] 的数对个数"""
            count = 0
            left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > distance:
                    left += 1
                    pass
                count += right - left
            return count

        # 二分查找
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right)/2
            count = count_distance_less_than(mid)
            if count >= k:
                right = mid
            elif count < k:
                left = mid + 1
                pass
            pass
        # return right  # Wrong
        return left


# ================================================================================
# ================================================================================

so = Solution()

print so.smallestDistancePair([1,3,8,44,6,7,12], 5)

# print so.smallestDistancePair(
#     [9,10,7,10,6,1,5,4,9,8,8,8,8],
#     18
# )
