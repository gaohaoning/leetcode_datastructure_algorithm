#!/usr/bin/env python
# coding:utf-8

"""
53. 最大子序和
难度
简单

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


# ================================================================================
# ================================================================================
"""
分治算法
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# ================================================================================
"""
动态规划：

Kadane 算法:
    该问题最早于1977年提出，
    但是直到1984年才被 卡耐基梅隆大学的教授 Jay Kadane 发现了线性时间的最优解法。
    所以算法虽然长度很短，但其实并不容易理解。

Kadane 算法的出发点:
    对于一个长度为 n 的数组 A 而言，从 A[0] 到 A[j] 是一个子数组（j<n），那么以 A[j] 结尾的子数组之最大和，
    要么是 A[j]， 要么是 max(A[i]~A[j-1]) + A[j] ，其中 0 ≤ i ≤ j-1 。

Kadane 算法具体思路:
    [1] 先将问题进行拆分， 
        指定数组中某一个元素 A[i] 作为最大子数列的末尾元素时，能找到的最大子数列的求和值是多少
    [2] 这样就会发现， 
        A[i] 作为末尾元素时能找到的最大子数列必然为:
        或是 A[i] 本身，
        或是 A[i-1] 作为末尾元素时能找到的最大子数列 subarray[i−1] 拼接上 A[i]
    [3] 所以我们只需要从头到尾遍历数组， 
        依次计算出每一个位置的 A[i] 作为末尾元素时， 能找到的最大子数列求和值 max_end_here_{i}, 
        就能在此基础上计算出 A[i+1] 作为末尾元素时， 能找到的最大子数列求和值 max_end_here_{i+1}, 
        在这一次遍历的过程中， 记录下 max_end_here 中的最大值就是全局最大子数列的求和值
"""


"""
时间复杂度: O(n)
空间复杂度: O(1)
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current = nums[0]
        max_all = nums[0]
        for x in nums[1:]:
            # 以 x 结尾的子数组，最大和
            max_current = max(x, x + max_current)
            # 所有已经遍历过的子数组，最大和
            max_all = max(max_current, max_all)
            pass
        return max_all


"""
时间复杂度: O(n)
空间复杂度: O(n)
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        """
        dp[i] 表示以 nums[i] 为结尾元素的最大子序列和
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(
                nums[i],
                dp[i-1] + nums[i]
            )
            pass
        return max(dp)
# ================================================================================
"""
最牛B的算法:
    真乃神人也 !!!
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
# ================================================================================


so = Solution()
print so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# 6
