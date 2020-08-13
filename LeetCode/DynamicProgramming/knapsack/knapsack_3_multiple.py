#!/usr/bin/env python
# coding:utf-8

"""
多重背包
    每个物品有不同的个数限制，例如：第 i 个物品的个数为 num[i]。
"""

# ================================================================================


n = 5  # 物品数量
v = 15  # 背包容量
weight = [5, 4, 7, 2, 6]  # 重量数组
value = [12, 3, 10, 3, 6]  # 价值数组
num = [2, 4, 1, 5, 3]  # 物品个数限制


def knapsack_dp(weight, value, n, v):
    # 矩阵尺寸: (n+1) * (v+1)
    # dp[i][j] 表示在前 i 个物品中，能够装入容量为 j 的背包中的最大价值
    dp = [[0 for _ in range(v + 1)] for _ in range(n + 1)]
    # 计算dp数组
    for i in range(1, n+1):
        for j in range(1, v+1):
            # ------------------------------
            # if j >= weight[i-1]:
            #     dp[i][j] = max(
            #         dp[i-1][j],  # 不要当前物品 i
            #         dp[i-1][j-weight[i-1]] + value[i-1]  # 要当前物品 i
            #     )
            # else:
            #     dp[i][j] = dp[i-1][j]  # 不要当前物品 i
            #     pass
            # ------------------------------
            # 物品 i 的最多个数，为以下二个值中的较小者
            num_max = min(
                num[i-1],
                j / weight[i - 1]
            )
            dp[i][j] = max(
                [
                    dp[i-1][j - k * weight[i-1]] + k * value[i-1] for k in range(num_max + 1)
                ]
            )
            # ------------------------------
            pass
        pass
    print '------------------------------'
    for x in dp:
        print x
        pass
    print '------------------------------'
    return dp[-1][-1]


print '背包承载的最大价值:'
print knapsack_dp(weight, value, n, v)
"""
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 12, 12, 12, 12, 12, 24, 24, 24, 24, 24, 24]
[0, 0, 0, 0, 3, 12, 12, 12, 12, 15, 24, 24, 24, 24, 27, 27]
[0, 0, 0, 0, 3, 12, 12, 12, 12, 15, 24, 24, 24, 24, 27, 27]
[0, 0, 3, 3, 6, 12, 12, 15, 15, 18, 24, 24, 27, 27, 30, 30]
[0, 0, 3, 3, 6, 12, 12, 15, 15, 18, 24, 24, 27, 27, 30, 30]
"""
# ================================================================================