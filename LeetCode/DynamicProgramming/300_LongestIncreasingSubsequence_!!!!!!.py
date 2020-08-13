#!/usr/bin/env python
# coding:utf-8

"""
300. 最长上升子序列
难度
中等


给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n^2) 。

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""

"""
LIS（Longest Increasing Subsequence）
"""

# ================================================================================
"""
动态规划
    思路:
        依次求出数组中每个元素作为结尾元素组成的子数组，最大上升子序列长度，组成数组 dp ，再求 dp 最大值。
        
    时间复杂度: O(n^2)
    空间复杂度: O(n)
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        """
        dp 表示: 以 nums[i] 为结尾的最长子序列长度。
        """
        dp = [1] * len(nums)
        """
        双层循环: 针对每个 i 值，遍历 nums[i] 之前的元素，更新 dp[i] 的值
        """
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(
                        dp[i],
                        dp[j] + 1
                    )
                    pass
                pass
            pass
        return max(dp)


# ================================================================================


"""
二分查找 + 动态规划    
    时间复杂度: O(nlogn)
    空间复杂度: O(n)
"""
"""
思路(非常难以理解):
    一种叫做 patience game 的纸牌游戏(甚至有一种排序方法就叫做 patience sorting（耐心排序）)
    
    首先，给你一排扑克牌，我们像遍历数组那样从左到右一张一张处理这些扑克牌，最终要把这些牌分成若干堆。
    处理这些扑克牌要遵循以下规则：
    
    只能把点数小的牌压到点数比它大的牌上。
    如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去。
    如果当前牌有多个堆可供选择，则选择最左边的堆放置。
    
    按照上述规则执行，可以算出最长递增子序列，牌的堆数就是最长递增子序列的长度（证明略）。
    
    我们只要把处理扑克牌的过程编程写出来即可。
    每次处理一张扑克牌不是要找一个合适的牌堆顶来放吗，牌堆顶的牌不是有序吗，这就能用到二分查找了：用二分查找来搜索当前牌应放置的位置。

参考:
    https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-she-ji-fang-fa-zhi-pai-you-xi-jia/
"""
"""
方法:
    [1] 维护一个数组 dp，放入 nums 数组的首元素；
    [2] 依次遍历 nums 数组:
            如果遍历的元素比 dp[-1] 大，直接追加到 dp 末尾；
            如果遍历的元素比 dp[-1] 小，则使用 binary search 找到 dp 中第一个[不小于]该元素的值，用该元素做替换。
    [3] 遍历完成后，dp 数组的长度即为 nums 数组的最大上升子序列长度。
    
注意：
    最终的数组 dp 不一定是 最大上升子序列 !!!!!
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
                left = mid + 1
            elif nums[mid] > target:
                # right = mid  # !!!!!
                right = mid - 1
            pass
        return right + 1  # 注意!

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                index = self.binary_search(dp, nums[i])
                dp.pop(index)
                dp.insert(index, nums[i])
                pass
            pass
        return len(dp)

# ================================================================================


test = [10, 9, 2, 5, 3, 7, 101, 18]
so = Solution()
print so.lengthOfLIS(test)
# 4


# ================================================================================
# ================================================================================

