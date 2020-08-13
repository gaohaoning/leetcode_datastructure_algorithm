#!/usr/bin/env python
# coding:utf-8

"""
283. 移动零
难度
简单

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
# ================================================================================
"""
思路:
    (不推荐)
时间复杂度:
    O(n**2)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    pass
                pass
            pass
        return nums
# ================================================================================
"""
思路:
    利用 filter
    (缺陷: 生成了额外的数组，不符合题目要求)
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 注意: 此处需要给 i 赋初值，以免第一个循环没有执行到
        i = 0
        for i, n in enumerate(filter(lambda x: x, nums)):
            nums[i] = n
            pass
        for j in range(i + 1, len(nums)):
            nums[j] = 0
            pass
        return nums
# ================================================================================
"""
思路:
    快慢指针
时间复杂度:
    O(n)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 注意: 此处需要给 i 赋初值
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                pass
            pass

        for n in range(i, len(nums)):
            nums[n] = 0
            pass
        return nums
# ================================================================================
# ================================================================================
# ================================================================================


print Solution().moveZeroes([0,1,0,3,12])
# [1, 3, 12, 0, 0]

print Solution().moveZeroes([1,2,3,1])
# [1, 2, 3, 1]

print Solution().moveZeroes([1,2,3,0,1,2])
# [1, 2, 3, 1, 2, 0]
