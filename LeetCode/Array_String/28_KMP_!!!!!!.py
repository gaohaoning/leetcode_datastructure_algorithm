#!/usr/bin/env python
# coding:utf-8

"""
28. 实现strStr()
难度
简单

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""
# ================================================================================
"""
思路:
    (利用 Python 函数，太 Low 不考虑了)
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            ret = haystack.index(needle)
        except ValueError, e:
            ret = -1
        return ret

# ================================================================================
"""
思路:
    (暴力求解，太 Low 不考虑了)
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ret = -1
        for i in range(len(haystack) - len(needle) + 1):
            is_match = True
            for j in range(len(needle)):
                if not haystack[i + j] == needle[j]:
                    is_match = False
                    break
                pass
            if is_match:
                return i
            pass
        return ret

# ================================================================================
"""
思路:
    KMP 算法 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
时间复杂度:
    O(m+n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def gen_F(t):
            """
            求F数组
            """
            f = [-1]
            i = 0
            j = -1
            while i < len(t):
                if j == -1 or t[i] == t[j]:
                    i += 1  # !!!!!!!!!!!!!!!!!!!!!!!!!
                    j += 1  # !!!!!!!!!!!!!!!!!!!!!!!!!
                    f.append(j)  # !!!!!!!!!!!!!!!!!!!!!!!!!
                else:
                    j = f[j]  # !!!!!!!!!!!!!!!!!!!!!!!!!
                    pass
                pass
            return f
        """
        KMP算法
        """
        l_haystack = len(haystack)
        l_needle = len(needle)
        i = 0
        j = 0
        f_array = gen_F(needle)
        while i < l_haystack and j < l_needle:
            if j == -1 or haystack[i] == needle[j]:
                i += 1  # !!!!!!!!!!!!!!!!!!!!!!!!!
                j += 1  # !!!!!!!!!!!!!!!!!!!!!!!!!
            else:
                j = f_array[j]  # !!!!!!!!!!!!!!!!!!!!!!!!!
                pass
            pass
        return i - j if j == l_needle else -1

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
s1 = 'abababca'
s2 = 'abc'
print so.strStr(s1, s2)
