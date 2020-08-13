#!/usr/bin/env python
# coding:utf-8

"""
485. 最大连续1的个数
难度
简单

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
"""
# ================================================================================
"""
思路:
    
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        count_max = 0
        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
                count_max = max(count, count_max)
            pass
        return count_max

# ================================================================================
"""
思路:

时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(map(lambda x: len(x), ''.join(map(str, nums)).split('0')))

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

# so = Solution()
# print so.findMaxConsecutiveOnes('1101111001')
# print so.findMaxConsecutiveOnes('101101')
