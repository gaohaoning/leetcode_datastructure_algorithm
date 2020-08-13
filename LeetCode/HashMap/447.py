#!/usr/bin/env python
# coding:utf-8

"""
447. 回旋镖的数量
难度
简单

给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""

# ================================================================================
"""
方法1:
    计算距离时不使用 cache，可以提交通过，但是效率低.
"""
"""
思路:
    逐个点遍历，计算其他点到此点的距离，计入counter，对于 counter 中 value 大于 2 的情况，计算排序数，累加。
时间复杂度:
    O(n**2)
空间复杂度: 
    O(n**2)
"""
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def calc_distance(m, n):
            """
            计算2个点的距离平方
            """
            if m > n:
                m, n = n, m
                pass
            return (points[m][0] - points[n][0])**2 + (points[m][1] - points[n][1])**2
        #
        total = 0
        for i, point in enumerate(points):
            counter_d_n = {}
            for j, point_another in enumerate(points):
                if i != j:
                    distance = calc_distance(i, j)
                    counter_d_n[distance] = counter_d_n.get(distance, 0) + 1
                    pass
                pass
            # counter_d_n
            for value in counter_d_n.values():
                if value >= 2:
                    total += value * (value - 1)
                pass
            pass
        #
        return total
# ================================================================================
"""
方法2:
    同方法1, 但是计算距离时添加 cache，减少重复计算。
    （但是执行时间反而变长了 ..., 所以推荐使用方法1 !!!）
"""
"""
思路:
    逐个点遍历，计算其他点到此点的距离，计入counter，对于 counter 中 value 大于 2 的情况，计算排序数，累加。
时间复杂度:
    O(n**2)
空间复杂度: 
    O(n**2)
"""


# class Solution(object):
#     def numberOfBoomerangs(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         def calc_distance(m, n, cache_ab_distance):
#             """
#             计算2个点的距离平方
#             """
#             if m > n:
#                 m, n = n, m
#                 pass
#             if (m, n) not in cache_ab_distance:
#                 distance = (points[m][0] - points[n][0])**2 + (points[m][1] - points[n][1])**2
#                 cache_ab_distance[(m, n)] = distance
#             else:
#                 distance = cache_ab_distance.get((m, n))
#             return distance
#         #
#         total = 0
#         cache_ab_distance = {}  # ========================= 当做 cache 来用
#         for i, point in enumerate(points):
#             counter_d_n = {}
#             for j, point_another in enumerate(points):
#                 if i == j:
#                     continue
#                     pass
#                 distance = calc_distance(i, j, cache_ab_distance)
#                 counter_d_n[distance] = counter_d_n.get(distance, 0) + 1
#                 pass
#             # counter_d_n
#             for d in counter_d_n:
#                 if counter_d_n[d] >= 2:
#                     total += counter_d_n[d] * (counter_d_n[d] - 1)
#                 pass
#             pass
#         #
#         print cache_ab_distance
#         return total


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
