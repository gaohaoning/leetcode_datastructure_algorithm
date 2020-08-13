#!/usr/bin/env python
# coding:utf-8

"""
动态规划
dynamic programming
"""

"""
动态规划解题思路:
    1.状态转移表
        回溯算法实现 - 定义状态 - 画递归树 - 找重复子问题 - 画状态转移表 - 根据递推关系填表 - 将填表过程翻译成代码
    2.状态转义方程
        找最优子结构 - 写状态转移方程 - 将状态转移方程翻译成代码
"""

"""
当拿到问题的时候，可以先用简单的回溯算法解决，然后定义状态，每个状态表示一个节点，然后画出对应的递归树。
从递归树中，很容易可以看出来，是否存在重复子问题，以及重复子问题是如何产生的。
以此来寻找规律，看是否能用动态规划解决。
"""

"""
1.状态转移表
    我们先画一个状态表。
    状态表一般是二维的，所以可以把它定义成二维数组。
    其中，每个状态包含三个变量: 行、列、数组值。
    我们根据决策的先后过程，从前往后，根据递推关系，分阶段填充表中的每个状态。
    最后，我们将这个递推填表的过程，翻译成代码，就是动态规划的代码了。

    (尽管大部分表都是二维的，但是如果问题的状态比较复杂，需要很多变量来表示，那对应的状态可能就是高维的，比如三维、四维。)
    (这时，就不适合用状态转移表法来解决了。一方面是因为高维状态转移表不好画图表示，另一方面因为人脑确实不擅长思考高维的东西。)
"""

"""
2.状态转义方程
    状态转移方程法有点类似递归的解题思路。
    我们需要分析，某个问题如何通过子问题来递归求解，也就是: 最优子结构。
    根据最优子结构，写出递归公式，也就是: 状态转移方程。
    有了状态转移方程，代码实现就非常简单了。
    一般情况下，我们有两种代码实现方法:
        1. 递归 + 备忘录
        2. 迭代递推
"""