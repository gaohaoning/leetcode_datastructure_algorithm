#!/usr/bin/env python
# coding:utf-8

"""
204. 计数质数

统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


# ================================================================================
# 笨方法, 穷举
class Solution(object):
    def is_prime(self, n):
        import math
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
            pass
        return True
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self.is_prime(i):
                count += 1
                pass
            pass
        return count

# ================================================================================
"""
素数普遍公式
公元前250年，古希腊的数学家 埃拉托塞尼 提出一种筛法：
“要得到不大于某个自然数N的所有素数，只要在2---N中将不大于 根号N 的素数的倍数全部划去即可”。
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        注意: 起始特殊值的处理
        (0 和 1 不是质数也不是合数)
        """
        if n <= 2:
            return 0
        l = [1] * n
        l[0:2] = [0, 0]
        for i in range(2, int(n**0.5) + 1):
            if l[i] == 1:
                l[i*i:n:i] = [0] * len(l[i*i:n:i])
                pass
            pass
        return sum(l)
# ================================================================================
# ================================================================================

