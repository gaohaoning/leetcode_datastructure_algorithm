#!/usr/bin/env python
# coding:utf-8

"""
498. 对角线遍历
难度
中等

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:



说明:

给定矩阵中的元素总数不会超过 100000 。
"""
# ================================================================================
"""
思路:
    各种便捷条件需要考虑清楚，不用算复杂度
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
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
        x, y = 0, 0
        # 方向 1:右上 -1:左下
        direction = 1
        ret = []
        # ret.append(matrix[x][y])
        while not (x == m or y == n):
            """
            1.加入当前元素
            2.移动光标
            """
            # print direction, '>>>>>', x, y
            """
            1.加入当前元素
            """
            ret.append(matrix[x][y])
            """
            2.移动光标
            """
            # 不需要掉头
            if direction == 1 and y < n - 1 and x > 0:
                x -= 1
                y += 1
            elif direction == -1 and x < m - 1 and y > 0:
                x += 1
                y -= 1
            # 需要掉头
            else:
                if direction == 1:
                    if y < n-1:
                        y += 1
                    elif y == n-1:
                        x += 1
                    pass
                elif direction == -1:
                    if x < m-1:
                        x += 1
                    elif x == m-1:
                        y += 1
                    pass
                direction = -direction
                pass
            pass
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
so = Solution()
print so.findDiagonalOrder(m)
