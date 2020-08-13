#!/usr/bin/env python
# coding:utf-8

"""
541. 反转字符串 II
难度
简单

给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。
"""
# ================================================================================
"""
思路:
    (参考 LeetCode 344)
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def reverse(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            pass
        return s

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        length = len(s)
        count = length/(2*k) + 1 if length % (2*k) else length/(2*k)
        for i in range(count):
            s[2*k*i: 2*k*i + k] = self.reverse(s[2*k*i: 2*k*i + k])
            pass
        return ''.join(s)


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.reverseStr("abcdefg", 2)
