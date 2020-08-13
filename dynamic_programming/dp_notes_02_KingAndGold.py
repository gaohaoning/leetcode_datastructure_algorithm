#!/usr/bin/env python
# coding:utf-8

"""
国王和金矿（本质上也是背包问题）

有一个国家发现了5座金矿，
参与挖矿工人的总数是10人，
每座金矿的黄金储量不同: [500, 200, 300, 350, 400]
需要参与挖掘的工人数也不同: [5, 3, 4, 3, 5]

每座金矿要么全挖，要么不挖，不能派出一半人挖取一半金矿。
要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？
"""
"""
"""
print '================================================================================'
"""
二维数组
"""

# 金矿数量
n = 5
# 工人数量
w = 10
# 金矿的黄金量
g = [500, 200, 300, 350, 400]
# 金矿的用工量
p = [5, 3, 4, 3, 5]

# dp 数组
dp = [[0] * (w+1) for _ in range(n)]
# dp = [[0] * (w+1) for _ in range(n)]


def show_dp():
    for x in dp:
        print x
        pass
    pass


# show_dp()

# 初始化 dp 数组第一行，作为边界
for j in range(w+1):
    dp[0][j] = g[0] if j >= p[0] else 0
    pass

# show_dp()

# 动态规划计算 dp 数组的剩余部分
for i in range(1, n):
    for j in range(1, w+1):
        if j >= p[i]:
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i-1][j-p[i]] + g[i]
            )
            pass
        else:
            dp[i][j] = dp[i-1][j]
            pass
        pass
    pass

show_dp()
"""
[0, 0, 0, 0, 0, 500, 500, 500, 500, 500, 500]
[0, 0, 0, 200, 200, 500, 500, 500, 700, 700, 700]
[0, 0, 0, 200, 300, 500, 500, 500, 700, 800, 800]
[0, 0, 0, 350, 350, 500, 550, 650, 850, 850, 850]
[0, 0, 0, 350, 350, 500, 550, 650, 850, 850, 900]
"""
print '================================================================================'
"""
一维数组
"""

# 金矿数量
n = 5
# 工人数量
w = 10
# 金矿的黄金量
g = [500, 200, 300, 350, 400]
# 金矿的用工量
p = [5, 3, 4, 3, 5]

# dp 数组
# dp = [[0] * (w+1) for _ in range(n)]
dp = [0] * (w+1)
print dp

# 初始化 dp 数组第一行，作为边界
for j in range(w+1):
    dp[j] = g[0] if j >= p[0] else 0
    pass
print dp


# 存储前一行的结果
# dp_pre = dp

# 动态规划计算 dp 数组的剩余部分
for i in range(1, n):
    # -------------------------
    # 存储前一行的结果
    # [1]
    # import copy
    # dp_pre = copy.copy(dp)
    # [2]
    dp_pre = [x for x in dp]
    # -------------------------
    for j in range(1, w+1):
        if j >= p[i]:
            dp[j] = max(
                dp_pre[j],
                dp_pre[j-p[i]] + g[i]
            )
            pass
        else:
            dp[j] = dp_pre[j]
            pass
        pass
    print dp
    pass

print '-------------------------'
print dp

print '================================================================================'
print '================================================================================'
print '================================================================================'
print '================================================================================'
