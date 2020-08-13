#!/usr/bin/env python
# coding:utf-8

"""
149. 直线上最多的点数
难度
困难

给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""
# ================================================================================
"""
思路:
    遍历所有点，针对每个点，求出：斜率相同的直线数量 + 重合点数 + 1
    最后取所有点的最大值。
时间复杂度:
    O(n**2)
空间复杂度: 
    O(n**2)
"""
"""
注意:
    求斜率时，使用 float 精度不够，需要使用 decimal 来计算 !!!
"""


class Solution(object):
    def slope(self, m, n, points, cache):
        """
        求两点斜率，带 cache
        （两点重合时不应该再求斜率）
        """
        from decimal import Decimal
        if m > n:
            m, n = n, m
            pass
        if (m, n) not in cache:
            # 注意: 处理特殊情况(斜率为无穷大)
            # 注意: 计算斜率时精度要够大（例如：[94911151,94911150],[94911152,94911151]）
            # ret = float('inf') if points[m][0] == points[n][0] else 1.0 * (points[m][1] - points[n][1]) / (points[m][0] - points[n][0])
            ret = float('inf') if points[m][0] == points[n][0] else Decimal(points[m][1] - points[n][1]) / Decimal(points[m][0] - points[n][0])
            cache[(m, n)] = ret
            # print m, n, '=====', ret
        else:
            ret = cache[(m, n)]
            pass
        return ret

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 注意: 处理特殊情况(0个点，1个点)
        if len(points) <= 1:
            return len(points)
        #
        max_points_in_line = 0
        cache_point_slope = {}  # 做 cache 用，避免重复计算
        for i, point in enumerate(points):
            counter_slope = {}
            n_same_point = 0
            for j, point_another in enumerate(points):
                if i != j:
                    # 注意：对于有重复点的情况，重复点的斜率可以算是和与其他点连线的斜率相同，就不应该单独去求斜率了
                    if points[i] == points[j]:
                        n_same_point += 1
                        pass
                    else:
                        v_slope = self.slope(i, j, points, cache_point_slope)
                        counter_slope[v_slope] = counter_slope.get(v_slope, 0) + 1
                        pass
                    pass
                pass
            # 注意: 处理特殊情况（所有点都重合，导致 斜率的计数器 counter_slope 为空）
            #
            # 处在同一直线的点数 = 斜率相同的直线数量 + 重合点数 + 1
            # max_i = max(counter_slope.values()) + 1
            # max_i = max(counter_slope.values()) + n_same_point + 1
            max_i = max(counter_slope.values()) + n_same_point + 1 if counter_slope else n_same_point + 1
            # print i, counter_slope, max_i

            max_points_in_line = max(max_i, max_points_in_line)
            pass
        return max_points_in_line

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()

# print so.maxPoints([[1,1],[1,1],[2,2],[2,2]])
#
# print so.maxPoints([[0,0],[0,0]])

print so.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])

# print 1.0 * 94911150/94911151
# print 1.0 * 94911151/94911152
