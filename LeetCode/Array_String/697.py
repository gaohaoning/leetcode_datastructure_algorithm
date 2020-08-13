#!/usr/bin/env python
# coding:utf-8

"""
697. 数组的度
难度
简单

给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
注意:

nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。
"""
# ================================================================================
"""
思路:
    (太复杂，不推荐！！！)
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        counter = {}
        memo = {}
        for i, x in enumerate(nums):
            if x not in memo:
                counter[x] = 1
                memo[x] = [i]
            else:
                counter[x] += 1
                memo[x].append(i)
                pass
            pass
        degree = max(counter.values())

        # print counter
        # print memo
        # print degree

        s = {}
        for k in counter:
            if counter[k] == degree:
                s[k] = memo[k][-1] - memo[k][0] + 1
                pass
            pass

        return min(s.values())

# ================================================================================
"""
思路:
    遍历统计
时间复杂度:
    O(5n)
空间复杂度: 
    O(3n)
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = len(nums)
        # 所有数字，第一次出现的索引
        left = {}
        # 所有数字，最后一次出现的索引
        right = {}
        # 计数器
        counter = {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
                pass
            right[x] = i
            counter[x] = counter.get(x, 0) + 1
            pass
        #
        degree = max(counter.values())
        for x in counter:
            if counter[x] == degree:
                ret = min(ret, right[x] - left[x] + 1)
                pass
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
so.findShortestSubArray([1,2,2,3,1])
