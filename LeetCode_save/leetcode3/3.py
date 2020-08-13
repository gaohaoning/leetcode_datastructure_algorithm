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
        maxlen = 0
        used = {}
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
                pass
            else:
                maxlen = max(maxlen, idx - start + 1)
                pass
            used[char] = idx
        return maxlen


so = Solution()
print so.lengthOfLongestSubstring('abcabcbb')
print so.lengthOfLongestSubstring('tmmzuxt')


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        used = {}
        for i, x in enumerate(s):
            # !!!!!
            if x not in used or used[x] < start:
                maxlen = max(maxlen, i - start + 1)
            elif used[x] >= start:
                start = used[x] + 1
                pass
            used[x] = i
            pass
        return maxlen


so = Solution()
print so.lengthOfLongestSubstring('abcabcbb')
print so.lengthOfLongestSubstring("tmmzuxt")
