#!/usr/bin/env python
# coding:utf-8

"""
54. 螺旋矩阵
难度
中等

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
# ================================================================================
"""
思路:
    (不要用记录路径的方法，其空间复杂度过高)
    按层扒皮
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 处理 行 或 列 为 0 或 1 的特殊情况
        m = len(matrix)
        if m == 0:
            return []
        elif m == 1:
            return matrix[0]
        n = len(matrix[0])
        if n == 0:
            return []
        elif n == 1:
            return [line[0] for line in matrix]
        # 一般情况
        # m > 1 and n > 1
        ret = []
        while not(len(matrix) == 0 or len(matrix[0]) == 0):
            x = len(matrix)
            y = len(matrix[0])
            # print '>>>>>', x, y
            # print matrix
            # print ret
            if x == 1 or y == 1:
                # 扒皮后，矩阵变成向量的情况
                for a in matrix:
                    for b in a:
                        ret.append(b)
                pass
            else:
                # 扒皮后，矩阵仍然是矩阵
                ret.extend(matrix[0])
                ret.extend([line[-1] for line in matrix[1:-1]])
                ret.extend(matrix[-1][::-1])
                ret.extend([line[0] for line in matrix[-2:0:-1]])
                pass
            matrix = [
                line[1:-1] for line in matrix[1:-1]
            ]
            pass
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
# m = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
m = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print so.spiralOrder(m)
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
