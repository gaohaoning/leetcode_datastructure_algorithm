#!/usr/bin/env python
# coding:utf-8

"""
59. 螺旋矩阵 II
难度
中等

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
# ================================================================================
"""
思路:
    按层扒皮()
    参考 LeetCode 54
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 被用来赋值的数字
        num = 1
        #
        ret = [[None]*n for _ in range(n)]
        matrix = [[None]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = (i, j)
                pass
            pass
        # print ret
        # print matrix
        while True:
            # 矩阵的阶
            order = len(matrix)
            if order == 0:
                # 扒皮后，矩阵为空
                break
            elif order == 1:
                # 扒皮后，矩阵变成只剩一个元素
                for a in matrix:
                    for b in a:
                        ret[b[0]][b[1]] = num
                        pass
                    pass
                break
            else:
                # 扒皮后，矩阵仍然是矩阵
                for xy in matrix[0] + \
                          [line[-1] for line in matrix[1:-1]] + \
                          matrix[-1][::-1] + \
                          [line[0] for line in matrix[-2:0:-1]]:
                    # print xy
                    ret[xy[0]][xy[1]] = num
                    num += 1
                    pass
                matrix = [
                    line[1:-1] for line in matrix[1:-1]
                ]
                pass
            pass
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
for line in so.generateMatrix(5):
    print line
    pass
