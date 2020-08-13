#!/usr/bin/env python
# coding:utf-8

"""
367. 有效的完全平方数
难度
简单

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
"""


# ================================================================================
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        left, right = 0, num/2 + 1
        while left <= right:
            mid = (left + right)/2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid - 1
                pass
            pass
        return False


# ================================================================================
# ================================================================================
# ================================================================================

