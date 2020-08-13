#!/usr/bin/env python
# coding:utf-8

"""
287. 寻找重复数
难度
中等

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n**2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


# ================================================================================
"""
思路1：
    先排序，再搜索。
    (不满足空间复杂度 O(1) !!! )

时间复杂度:
    O(n * logn)

空间复杂度:
    O(n)
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

# ================================================================================
"""
思路2：
    集合
    (不满足空间复杂度 O(1) !!! )

时间复杂度:
    O(n)
空间复杂度:
    O(n)
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)

# ================================================================================
"""
思路3:
    Cycle Detection
    根据题干:
        给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
        假设只有一个重复的整数，找出这个重复的数。
    将问题转化为：
        求环形链表的入环点(LeetCode 142), 用快慢指针法解决。
    
时间复杂度:
    O(n)
空间复杂度:
    O(1)
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while fast <= len(nums) - 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                s1 = 0
                s2 = slow
                while s1 != s2:
                    s1 = nums[s1]
                    s2 = nums[s2]
                    pass
                return s1
                pass
            pass

# ================================================================================
# ================================================================================
# ================================================================================

