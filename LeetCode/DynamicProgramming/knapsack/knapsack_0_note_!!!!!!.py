#!/usr/bin/env python
# coding:utf-8

"""
knapsack（背包问题）
"""

"""
背包问题(Knapsack problem)

    给定一组物品，每种物品都有自己的重量(weight)和价格(value)，在限定的总重量内，我们如何选择，才能使得物品的总价格最高。
    
    问题的名称来源于如何选择最合适的物品放置于给定背包中。
    相似问题经常出现在商业、组合数学，计算复杂性理论、密码学和应用数学等领域中。
    也可以将背包问题描述为决定性问题，即在总重量不超过 W 的前提下，总价值是否能达到 V ？
"""

"""
问题分类:

01背包
    每个物品只能选择取或不取，即只能取 0个 或 1个。
        
完全背包
    每个物品可以取无限次，只要加起来总容量不超限即可。
    
多重背包
    每个物品有不同的个数限制，例如：第 i 个物品的个数为 num[i]。
"""


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================