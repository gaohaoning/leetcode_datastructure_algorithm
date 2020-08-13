#!/usr/bin/env python
# coding:utf-8

"""
121. 买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


# ================================================================================
"""
暴力穷举法(超出时间限制)

Time complexity : O(n^2)
Space complexity : O(1) 
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                profit = max(profit, prices[j] - prices[i])
                pass
            pass
        return profit
# ================================================================================
"""
(一次)遍历数组，维护一个变量记录已经遍历过的最小值，每次将非最小值与前面的最小值做差，记录最大收益。

Time complexity : O(n)
Space complexity : O(1) 
"""
class Solution(object):
    def maxProfit(self, prices):
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

# ================================================================================
"""
动态规划方法:
(此例题是最朴素的动态规划)
"""
"""
最多只允许完成一笔交易
"""
"""
动态规划2部曲:
    1.状态定义:
        max_profit: mp
            (二维数组)
                i (第一维表示第 i 天，0<-i<=n-1)
                j (第二维表示是否拥有股票, j = 0[没有买入] 或 1[买入没卖] 或 2[买入又卖出])
    2.状态转移公式:
        # 今天结束后没有股票
        mp[i, 0] = max(
            mp[i-1, 0],  # 前一天没有股票，今天不动
            mp[i-1, 1] + prices[i]  # 前一天有股票，今天卖出
        )
        # 今天结束后有股票
        mp[i, 1] = max(
            mp[i-1, 1],  # 前一天有股票，今天不动
            mp[i-1, 0] - prices[i]  # 前一天没有顾，今天买入
        )
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
        ret = 0
        """
        二维状态空间初始化
        """
        profit = [
            [0 for i in range(3)] for j in range(len(prices))
        ]
        """
        1.边界
        """
        profit[0][0] = 0  # 没买
        profit[0][1] = -prices[0]  # 买入股票
        profit[0][2] = 0  # 买入卖出 == 没买
        """
        2.状态转移公式:
        """
        for i in range(1, len(prices)):
            profit[i][0] = profit[i-1][0]  # 前一天没有今天也没买
            profit[i][1] = max(profit[i - 1][1], profit[i-1][0] - prices[i])  # max(前一天有今天没动，前一天没有今天买入)
            profit[i][2] = profit[i-1][1] + prices[i]  # 前一天有今天卖出
            ret = max(
                ret,
                profit[i][0],
                profit[i][1],
                profit[i][2]
            )
            pass
        return ret
# ================================================================================
