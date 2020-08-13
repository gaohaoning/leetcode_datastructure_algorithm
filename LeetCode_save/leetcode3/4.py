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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxl = 0
        maxs = ''
        used = {}
        for i, x in enumerate(s):
            # 注意: 要考虑的情况: x in used and used[x] < start
            if x not in used or used[x] < start:
                maxl = max(maxl, i - start + 1)
                maxs = s[start: i + 1]
            else:
                start = used[x] + 1
                pass
            used[x] = i
            pass
        print maxs
        return maxl


so = Solution()
print so.lengthOfLongestSubstring('abcabcbb')
print so.lengthOfLongestSubstring('bbbbb')
print so.lengthOfLongestSubstring('pwwkew')

