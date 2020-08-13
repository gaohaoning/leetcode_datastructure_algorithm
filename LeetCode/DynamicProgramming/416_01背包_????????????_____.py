#!/usr/bin/env python
# coding:utf-8

"""
416. 分割等和子集
难度
中等

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].


示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
"""
# ================================================================================
"""
思路:
    动态规划: 0-1背包
    (二维DP数组)
时间复杂度:
    O(NC)
    这里 N 是数组元素的个数，C 是数组元素的和的一半。
空间复杂度: 
    O(NC)
    这里 N 是数组元素的个数，C 是数组元素的和的一半。
"""

"""
dp 数组维度:
    len(nums) * (sum/2 + 1)

dp[i][j]
    表示能否 (True or False) 从数组的 [0, i] 这个子区间内挑选一些正整数(每个数只能用一次)，使得这些数的和等于 j。

根据我们学习的 0-1 背包问题的状态转移推导过程，新来一个数，例如是 nums[i]，根据这个数可能选择也可能不被选择：
    如果不选 nums[i]，在 [0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j ，那么 dp[i][j] = true
    如果选择 nums[i]，在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]

状态转义方程:
    if j >= nums[i]:
        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
    else:
        dp[i][j] = dp[i - 1][j]
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        l = len(nums)
        if s % 2:
            return False
        # 二维 dp 问题: 背包容量
        target = s/2
        dp = [[False for _ in range(target + 1)] for _ in range(l)]
        # 先写第 1 行：看看第 1 个数是不是能够刚好填满容量为 target
        for j in range(target + 1):
            dp[0][j] = True if nums[0] == j else False
            pass
        # 再写其余的行
        # i 为物品索引，j 为容量
        for i in range(1, l):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
                pass
            pass
        # print '------------------------------'
        # for x in dp:
        #     print x
        #     pass
        # print '------------------------------'
        return dp[-1][-1]

# ================================================================================
"""
思路:
    动态规划: 0-1背包
    (一维DP数组)
时间复杂度:
    O(NC)
    这里 N 是数组元素的个数，C 是数组元素的和的一半。
空间复杂度: 
    O(C)
    这里 N 是数组元素的个数，C 是数组元素的和的一半。
    减少了物品那个维度，无论来多少个数，用一行表示状态就够了。
"""


# TODO: ??????????????????????????????????????????????????


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.canPartition([1, 5, 11, 5])
# print so.canPartition([1, 5, 3])
# print so.canPartition([100])
