#!/usr/bin/env python
# coding:utf-8

"""
220. 存在重复元素 III
难度
中等

给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""
# ================================================================================
"""
思路:
    查找表 + 滑动窗口
时间复杂度:
    O(n*k)
空间复杂度: 
    O(k)
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # 处理特殊情况
        if not nums or k <= 0 or t < 0:
            return False
        #
        window = []
        for i, n in enumerate(nums):
            # 逻辑判断
            if t == 0:
                if n in window:
                    return True
            else:
                for x in window:
                    if abs(x - n) <= t:
                        return True
            # 维护窗口
            if i >= k:
                window.pop(0)
                pass
            window.append(n)
            pass
        return False

# ================================================================================
"""
更优解法 !!!!!!!!!!

思路:
    （类似 bucket 排序的思路）
    （有待理解 ??????????）
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # 处理特殊情况
        if not nums or k <= 0 or t < 0:
            return False
        #
        if t == 0:
            # LeetCode 219
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
        else:
            # t != 0
            bucket = {}
            for i, num in enumerate(nums):
                bucket_id = num / t
                # [1] 逻辑判断
                for near_by in (bucket_id - 1, bucket_id, bucket_id + 1):
                    if near_by in bucket and abs(bucket[near_by] - num) <= t:
                        return True
                # [2] 维护 bucket
                #     We don't need to store multiple values in a bucket.
                #     Because if that is a case, we should return True above.
                #     We always update the bucket with the latest (right most) value.
                bucket[bucket_id] = num
                if i >= k:
                    expired = nums[i - k] / t
                    del bucket[expired]

            return False
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)
