#!/usr/bin/env python
# coding:utf-8

"""
118. 杨辉三角
难度
简单

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
# ================================================================================
"""
思路:
    (数学知识)二项式定理
    参考 LeetCode 119
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def c_n_m(n, m):
            """
            求组合数
            """
            # 存储需要用到的: 阶乘计算结果
            dict_factorial = {0: 1}
            for i in range(1, rowIndex/2 + 2):
                if i not in dict_factorial:
                    dict_factorial[i] = dict_factorial[i - 1] * i
                    pass
                pass
            # print dict_factorial
            # 计算组合数
            if m > n / 2:
                m = n - m
                pass
            ret = 1
            for x in range(n - m + 1, n + 1):
                ret *= x
                pass
            ret = ret/dict_factorial[m]
            return ret
        # print c_n_m(numRows, 2)
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            ret = []
            # 注意题目描述的行数与组合数分母 n 的对应关系
            # n = rowIndex - 1
            n = rowIndex
            for i in range(n + 1):
                if i <= n/2:
                    ret.append(c_n_m(n, i))
                    pass
                else:
                    ret.append(ret[n - i])
                    pass
                pass
            return ret

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for n in range(numRows):
            ret.append(self.getRow(n))
            pass
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.generate(5)
