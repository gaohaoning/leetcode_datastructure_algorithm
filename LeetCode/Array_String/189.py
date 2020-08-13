#!/usr/bin/env python
# coding:utf-8

"""
189. 旋转数组
难度
简单

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""
# ================================================================================
"""
思路:
    切片法
时间复杂度:
    O(1)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        if k == 0:
            return
        tmp = nums[:-k]
        nums[:k] = nums[-k:]
        nums[k:] = tmp
# ================================================================================
"""
思路:
    取得表尾元素插入表头，重复 k 次
时间复杂度:
    O(k)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        for _ in range(k):
            element = nums.pop()
            nums.insert(0, element)
            pass


# ================================================================================
"""
思路:
    翻转法：
        1.全表反转
        2.前 k 个元素反转
        3.后 n-k 个元素反转
时间复杂度:
    O(n)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def reverse(self, array, start, stop):
        """
        双指针反转
        """
        while start < stop:
            array[start], array[stop] = array[stop], array[start]
            start += 1
            stop -= 1
            pass

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

n = [1,2,3,4,5,6,7]
k = 3

# n = [1]
# k = 0

Solution().rotate(n, k)
print n
