#!/usr/bin/env python
# coding:utf-8

"""
290. 单词模式

给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false

说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
"""


# ================================================================================
"""
普通解法
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ls = str.split()
        if len(pattern) != len(ls) or len(set(pattern)) != len(set(ls)):
            return False
        #
        used = {}
        for k, v in zip(pattern, ls):
            if k not in used:
                used[k] = v
                pass
            elif used[k] != v:
                return False
            pass
        return True


# ================================================================================
"""
牛逼解法
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ls = str.split()
        z = zip(pattern, ls)
        return len(pattern) == len(ls) and len(set(pattern)) == len(set(ls)) == len(set(z))
# ================================================================================
# ================================================================================

