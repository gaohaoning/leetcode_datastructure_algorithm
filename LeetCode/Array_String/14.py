#!/usr/bin/env python
# coding:utf-8

"""
14. 最长公共前缀
难度
简单

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
# ================================================================================
"""
思路:
    (笨方法)
时间复杂度:
    O(k*n)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        s = strs[0]
        if not s:
            return ''
        #
        prefix = ''
        for i in range(len(s)):
            is_common = True
            # prefix = s[:i + 1]
            for ss in strs[1:]:
                if ss[:i + 1] != s[:i + 1]:
                    is_common = False
                    break
                pass
            if not is_common:
                break
            else:
                prefix = s[:i + 1]
            pass
        return prefix
# ================================================================================
"""
思路:
    利用 Python 的 zip 和 set
时间复杂度:
    O(k*n)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        c = 0
        for z in zip(*strs):
            # print z
            count = len(set(z))
            if count == 1:
                c += 1
            else:
                break
            pass
        return strs[0][:c]


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.longestCommonPrefix(["flower","flow","flight"])
