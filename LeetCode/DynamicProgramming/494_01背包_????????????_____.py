#!/usr/bin/env python
# coding:utf-8

"""
494. 目标和
难度
中等

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
注意:

数组的长度不会超过20，并且数组中的值全为正数。
初始的数组的和不会超过1000。
保证返回的最终结果为32位整数。
"""
# ================================================================================
"""
思路:
    (转化为0-1背包问题，使用 DP 求解)
    (dp 为二维数组)
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        """
        一定没有解的情况:
            sum+S为奇数
            S大于sum
        """
        sum_nums = sum(nums)
        len_nums = len(nums)
        if (sum_nums + S) % 2 or sum_nums < S:
            return 0
        """
        转化为背包问题:
            物品: nums 中所有元素
            背包容量: -sum_nums ~ sum_nums
        网格维度是:
            (len_nums + 1) * (2 * sum_nums + 1)
        """
        dp = [[0] * (2 * sum_nums + 1) for _ in range(len_nums + 1)]
        # 先处理第一行
        # 从 nums 数组中什么也不选，目标和为 0，方案数为 1
        dp[0][sum_nums] = 1
        # 再处理其他行
        for i in range(1, len_nums + 1):
            for j in range(2 * sum_nums + 1):
                # ------------------------------
                # TODO: ??????????????????????????????????????????????????
                if j + nums[i-1] < 2 * sum_nums + 1:
                    dp[i][j] += dp[i-1][j + nums[i-1]]
                    pass
                if j - nums[i-1] >= 0:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
                    pass
                # TODO: ??????????????????????????????????????????????????
                # ------------------------------
                pass
            pass
        return dp[len_nums][sum_nums + S]


# ================================================================================
"""
思路:
    (转化为动态规划问题 DP)
    (dp 为一维数组)
    在某个解中正数和为x，负数和的绝对值为y，则x+y=sum，x-y=S，解得x=(sum+S)/2
    所以就有在nums中选择一部分数（装与不装到背包中），让其和为x（总的容量为x），此时转化为了0-1 【背包问题】, 
    剩余部分数据和当然为y，所以x+y=sum，x-y=S（y中的数都去负号）
    同时可有sum+S为奇数，则一定没有解的推论，因为要除以2才是x的解
    
时间复杂度:
    O()
空间复杂度: 
    O()
"""


# TODO: ??????????????????????????????????????????????????


# class Solution(object):
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         """
#         一定没有解的情况:
#             sum+S为奇数
#             S大于sum
#         """
#         if (sum(nums) + S) % 2 or sum(nums) < S:
#             return 0
#         """
#         问题转化为:
#         从 nums 中找到一些数，使其和为 target = (sum(nums) + S)/2
#         """
#         """
#         注意:
#         需要关注数组中有 0 的情况，现将 n0 个 0 元素取出，然后在最终结果中乘以 2**n0 即可
#         """
#         n0 = nums.count(0)
#         nums = [n for n in nums if n != 0]
#         target = (sum(nums) + S) / 2
#         """
#         动态规划算法(DP)
#         """
#         # ------------------------------
#         dp = [1] + [0] * target
#         for i in range(len(nums)):
#             for j in range(target, nums[i] - 1, -1):
#                 dp[j] += dp[j - nums[i]]
#                 pass
#             pass
#         # ------------------------------
#         return dp[target] * 2**n0


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.findTargetSumWays(
    [1,1,1,1,1],
    3
)
