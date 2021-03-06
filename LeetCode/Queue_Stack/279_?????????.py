#!/usr/bin/env python
# coding:utf-8

"""
279. 完全平方数
难度
中等

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""

# ================================================================================
"""
数学知识:
    (拉格朗日)四平方数和定理:
        任何一个正整数都可以表示成不超过四个整数的平方之和。
"""
# ================================================================================
# TODO: 尚未完全理解 ？？？？？？？？？？

"""
题目分析:
    任何数字都可以表示成为一个普通数字加上一个完全平方数;
    dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])

思路:
    动态规划(dp)
        dp[i]: 
            组成正整数 i 的完全平方数的最小个数
        初始条件:
            dp[0]=0;
            dp[1]=1;
        动态转移方程:
            dp[i]=min(dp[i], dp[i-j*j]+1),其中j*j<=i.

时间复杂度:
    O( n*sqrt(n) )
    O( n**(3/2) )  
空间复杂度: 
    O( n )
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        # dp 数组的初始状态，第 x 位的初始值设为 x (因为最坏的情况下，n 也就由 n 个 1 构成)
        dp = [x for x in range(n+1)]
        # dp[0] = 0
        # dp[1] = 1
        for i in range(2, n+1):
            # ------------------------------
            j = 1
            while j*j <= i:
                dp[i] = min(
                    dp[i],
                    dp[i - j*j] + 1
                )
                j += 1
                pass
            # ------------------------------
            pass
        return dp[n]


# ================================================================================
# TODO: 尚未完全理解 ？？？？？？？？？？？？？？？？？？？？

"""
题目分析:
    这是一个图论问题，0到n看作n+1图的n+1个节点
        若一个点的值加上平方数就能到另外一个点，
        那么在两个点之间连一条边，且权值为1。
    问题转化为:
        从 0点 到 n点 的最短距离（求图的最短路径问题），适合用bfs来处理。
"""
"""
思路:
    BFS(广度优先搜索)
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    # TODO: 尚未完全理解 ？？？？？？？？？？？？？？？？？？？？
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 队列
        from collections import deque
        queue = deque()
        queue.append(0)
        # dist 记录每个节点到0的距离
        # 这样不行:
        # dist = [n for _ in range(n+1)]
        dist = [n + 1 for _ in range(n+1)]
        dist[0] = 0
        #
        while queue:
            t = queue.popleft()
            if t == n:
                return dist[t]
            # ------------------------------
            # 找到当前节点所有的子节点
            i = 1
            while t + i*i <= n:
                j = t + i*i
                if dist[j] > dist[t] + 1:
                    # 现在已经确定节点j到节点t的距离为1
                    dist[j] = dist[t] + 1
                    queue.append(j)
                    pass
                i += 1
                pass
            # ------------------------------
            pass
        return 0


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
