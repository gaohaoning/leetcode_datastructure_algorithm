#!/usr/bin/env python
# coding:utf-8

"""

123. 买卖股票的最佳时机 III
难度
困难

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 [[[两笔]]] 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
"""


# ================================================================================
"""
方法1:
拆分数组，然后用 leetcode 121 的方法求解子问题，求和
（此方法可以通过测试用例，但正式提交会导致超时）
"""
class Solution(object):
    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = max(profit, prices[i] - low)
                pass
            pass
        return profit
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        length = len(prices)
        profit_max = 0
        for i in range(length):
            sub1 = prices[:i]
            sub2 = prices[i:]
            profit = self.maxProfit_1(sub1) + self.maxProfit_1(sub2)
            profit_max = max(profit_max, profit)
            pass
        return profit_max

# ================================================================================
# TODO: 此方法尚未完全理解 ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

"""
方法2:
动态规划，公式推导
"""
"""
状态方程(状态转移公式):
    b1 = max(b1,     -prices[i])
    s1 = max(s1, b1 + prices[i])
    b2 = max(b2, s1 - prices[i])
    s2 = max(s2, b2 + prices[i])

边界:
    b1 = -prices[0]
    s1 = 0  （相当于买入后再卖出）
    b2 = -prices[0]  （相当于买入后再卖出再买入）
    s2 = 0  （相当于买入后再卖出再买入再卖出）
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        #
        b1 = -prices[0]
        s1 = 0
        b2 = -prices[0]
        s2 = 0
        #
        for i in range(1, len(prices)):
            b1 = max(b1, -prices[i])
            s1 = max(s1, b1 + prices[i])
            b2 = max(b2, s1 - prices[i])
            s2 = max(s2, b2 + prices[i])
            pass
        return s2

# ================================================================================
# ================================================================================


p = [3, 3, 5, 0, 0, 3, 1, 4]
so = Solution()
print so.maxProfit(p)
# should be 6
