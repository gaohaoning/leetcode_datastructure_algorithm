#!/usr/bin/env python
# coding:utf-8

"""
动态规划
    动态规划(dynamic programming)是运筹学的一个分支，是求解决策过程(decision process)最优化的数学方法。
"""
"""
分治 和 动态规划 区别:
    分治，是将问题划分为 [互不相交的] 子问题，递归的求解子问题，再将它们的解组合起来，求出原问题的解。
    动态规划，是应用于 [子问题重叠] 的情况，即不同的子问题具有公共的子子问题。(例如 Fibonacci）
"""
"""
例如对于 Fibonacci 的例子，
    递归的求解方式就是分治算法，由于它的子问题是相互相关的，此时利用分治法就做了很多重复的工作，它会反复求解那些公共子子问题。
    而动态规划算法对每一个子子问题只求解一次，将其保存在一个表格中，从而避免重复计算。
"""

"""
下面介绍两种方法来说明动态规划的算法：
    自顶向下的备忘录法
    自底向上的方法
"""
# ================================================================================
"""
递归(分治)
"""

def fibonacci(n):
    # 递归终止条件
    if n == 0 or n == 1:
        return 1
    # 当前层级的处理逻辑
    # 递归调用
    return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(9)  # 55
# ================================================================================
"""
自顶向下的备忘录法
"""

def fibonacci(n):
    memo = [None] * (n + 1)
    return fib(n, memo)


def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    memo[n] = 1 if n <= 1 else fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


print fibonacci(9)
# 55


"""
在动态规划当中包含三个重要的概念：
    最优子结构
    边界
    状态转移公式

对于上面这个算法来说，
    meno[10]的最优子结构就是fib(9,meno)和fib(8,meno)了；
    边界就是meno[2]与meno[1]了；
    状态转移方程就是meno[n] = fib(n - 1, meno) + fib(n - 2, meno)。

注意最优子结构和状态转移方程的区别，
    最优子结构是针对具体某个值来说的;
    状态方程就是它的那个整体的推算方程。
"""
# ================================================================================
"""
自底向上的方法
"""
"""
自顶而下的方式来计算最终的结果，还是有一个递归的过程。
既然最终是从fib(1)开始算，那么直接从fib(1)计算不就得了，先算子问题，再算父问题。
"""

def fibonacci(n):
    memo = [None] * (n + 1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
        pass
    return memo[n]


print fibonacci(9)
# 55

"""
自底向上的方法(节省空间版)
"""
def fibonacci(n):
    if n <= 1:
        return 1
    fib_2 = 1
    fib_1 = 1
    for i in range(2, n + 1):
        #
        # fib_2, fib_1, fib = fib_1, fib_2 + fib_1, fib_2 + fib_1
        #
        fib = fib_2 + fib_1
        fib_2 = fib_1
        fib_1 = fib
        pass
    return fib
print fibonacci(9)
# ================================================================================

