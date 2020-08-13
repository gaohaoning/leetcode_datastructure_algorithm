#!/usr/bin/env python
# coding:utf-8

"""
49. 字母异位词分组
难度
中等

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""
# ================================================================================
"""
思路:
    
时间复杂度:
    O(N*K)
空间复杂度: 
    O(N)
其中 N 是 strs 的长度，而 K 是 strs 中字符串的最大长度。
"""
"""
注意: 涉及字母，使用计数元组更加节省空间 !!!
    ord('a') = 97
    ord('z') = 122
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_tuple_str = {}
        for s in strs:
            s_tuple = [0] * 26
            for x in s:
                s_tuple[ord(x) - 97] += 1
                pass
            s_tuple = tuple(s_tuple)
            # 注意: dict_tuple_str 的赋值方法 !!!
            if s_tuple in dict_tuple_str:
                dict_tuple_str[s_tuple].append(s)
            else:
                dict_tuple_str[s_tuple] = [s]
            pass
        # print dict_tuple_str
        ret = []
        for k in dict_tuple_str:
            ret.append(dict_tuple_str[k])
            pass
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
