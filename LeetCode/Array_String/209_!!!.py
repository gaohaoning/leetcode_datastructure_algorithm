#!/usr/bin/env python
# coding:utf-8

"""
209. 长度最小的子数组
难度
中等

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
# ================================================================================
"""
思路:
    双指针(滑动窗口)
时间复杂度:
    O(n)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        min_len = len(nums)
        vsum = 0
        is_found = False
        while right < len(nums):
            # print left, right, min_len, nums[left: right + 1]
            vsum += nums[right]
            if vsum >= s:
                is_found = True
                min_len = min(min_len, right - left + 1)
                while vsum >= s:
                    min_len = min(min_len, right - left + 1)
                    vsum -= nums[left]
                    left += 1
                    pass
                pass
            # 必须每次都滑动窗口右边界
            right += 1
            pass
        return min_len if is_found else 0
# ================================================================================
"""
思路:
    二分查找
时间复杂度:
    O(n*log(n))
空间复杂度: 
    O(log(n))
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)
        while left < right:
            mid = (left + right)/2
            # ----------------------------------------
            # 求 mid 长度的子数组和的最大值
            max_sum = 0
            ss = 0
            for i, n in enumerate(nums):
                ss += n
                if i >= mid:
                    ss -= nums[i - mid]
                    pass
                max_sum = max(max_sum, ss)
                pass
            # ----------------------------------------
            # print left, right, 'mid=%s' % mid, 'max_sum=%s' % max_sum
            # ----------------------------------------
            if max_sum < s:
                left = mid + 1
            else:
                right = mid
                pass
            pass
        # left == right
        return left if sum(nums) >= s else 0


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.minSubArrayLen(7, [2,3,1,2,4,3])
# 2
print so.minSubArrayLen(3, [1,1])
# 0
