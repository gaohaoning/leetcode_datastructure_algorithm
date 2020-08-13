#!/usr/bin/env python
# coding:utf-8

"""
给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

示例 1：

输入：[1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。
 
注：
输入数组只包含 0 和 1.
输入数组的长度为正整数，且不超过 10,000
 
进阶：
如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？

"""
# ================================================================================
"""
思路:
    
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_len = map(lambda x: len(x), ''.join(map(str, nums)).split('0'))
        max_len = 0
        for i in range(len(list_len) - 1):
            max_len = max(max_len, list_len[i] + list_len[i + 1])
            pass
        return max_len + 1

# ================================================================================
"""
思路:
    由于可以允许翻转一次0，所以我们记录两部分内容：
    zeroLeft 表示在需要翻转的0之前的连续1的个数，zeroRight 表示在需要翻转的0之后的连续1的个数。
    一旦我们遇到一个0，就需要更新 zeroLeft 和 zeroRight 了。
    最终只要记录下来 zeroLeft + zeroRight 的最大值即可。
    注意到这里我们让 zeroRight 同时包含了需要翻转的0，这样就可以统一处理只有一个0的情况了。
    
    算法的时间复杂度是O(n)，空间复杂度是O(1)。
    由于我们不需要对原来出现的数据进行重新存取，所以这个代码也满足了Follow up的要求，可以处理无限长的数据流。
时间复杂度:
    O(n)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        ret = 0
        for n in nums:
            if n == 1:
                right += 1
            else:
                ret = max(ret, left + right)
                left = right
                right = 0
                pass
            pass
        return ret + 1

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.findMaxConsecutiveOnes([1,0,1,1,0])
# 4
print so.findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,1,0,0,1])
# 7
