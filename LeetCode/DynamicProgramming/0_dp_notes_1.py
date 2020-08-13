#!/usr/bin/env python
# coding:utf-8

"""
动态规划
dynamic programming
"""

"""
动态规划表面上很难，其实存在很简单的套路：
    当求解的问题满足以下两个条件时，就应该使用动态规划：
        [1] 主问题的答案 包含了 可分解的子问题答案（也就是说，问题可以被递归的思想求解）
        [2] 递归求解时， 很多子问题的答案会被多次重复利用

动态规划的本质思想就是：递归。
    但是如果直接应用递归方法，子问题的答案会被重复计算产生浪费，同时递归更加耗费栈内存； 
    所以通常用一个二维矩阵（表格）来表示不同子问题的答案，以实现更加高效的求解。
"""

"""
动态规划三要素:
    以 fibonacci 为例，对于 fib(n) = fib(n-1) + fib(n-2)
        [1] 最优子结构
            fib(n-1)、fib(n-2) 是 fib(n) 的最优子结构
        [2] 边界
            fib(1)=1、fib(2)=2 是问题的边界
        [3] 状态转移方程
            fib(n) = fib(n-1) + fib(n-2)
"""

"""
动态规划小结:
    需要在给定约束条件下优化某种指标时，动态规划很有用。
    问题可分解为离散子问题时，可使用动态规划来解决。
    每种动态规划解决方案都涉及网格。
    单元格中的值通常就是你要优化的值。
    每个单元格都是一个子问题，因此你需要考虑如何将问题分解为子问题。
    没有放之四海皆准的计算动态规划解决方案的公式。
"""
