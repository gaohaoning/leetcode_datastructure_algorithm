#!/usr/bin/env python
# coding:utf-8

"""
451. 根据字符出现频率排序
难度
中等

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
"""
# ================================================================================


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = {}
        for x in s:
            counter[x] = counter.get(x, 0) + 1
            pass
        counter_tuple = [(k, v) for k, v in counter.iteritems()]
        ret = ''
        for ct in sorted(counter_tuple, key=lambda ss: ss[1], reverse=True):
            ret += ct[0] * ct[1]
            pass
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

