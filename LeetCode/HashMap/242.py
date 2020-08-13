#!/usr/bin/env python
# coding:utf-8

"""
242. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


# ================================================================================
# 直接用现成的 Counter 类
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        return cs == ct
# ================================================================================
"""
自己实现 counter
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter_s = {}
        counter_t = {}
        for x in s:
            counter_s[x] = counter_s.get(x, 0) + 1
        for x in t:
            counter_t[x] = counter_t.get(x, 0) + 1
            pass
        return counter_s == counter_t
# ================================================================================
"""
最优解法

ord(c)
    Given a string of length one, 
    return an integer representing the Unicode code point of the character when the argument is a unicode object, 
    or the value of the byte when the argument is an 8-bit string. 
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        # 注意: 此处需要创建2个list，不能这样: cs = ts = [0] * 26
        cs = [0] * 26
        ts = [0] * 26
        for x, y in zip(s, t):
            cs[ord(x) - ord('a')] += 1
            ts[ord(y) - ord('a')] += 1
            pass
        return cs == ts

# ================================================================================

