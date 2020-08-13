#!/usr/bin/env python
# coding:utf-8

"""
无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


"""

class Solution(object):
    def longest_sub(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        sub = ''
        length = 0
        for n in range(0, l):
            sub = s[:n + 1]
            if len(set(sub)) != n + 1:
                # repeat
                break
                pass
            else:
                length = n + 1
                pass
            pass
        return length

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        length = 0
        for start in range(0, l - 1):
            new_length = self.longest_sub(s[start:])
            length = new_length if new_length > length else length
            pass
        return length


so = Solution()
print so.lengthOfLongestSubstring('bbbbb')

