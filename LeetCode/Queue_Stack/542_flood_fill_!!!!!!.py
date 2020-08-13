#!/usr/bin/env python
# coding:utf-8

"""
542. 01 矩阵
难度
中等

给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""

# ================================================================================
"""
思路:
    (有点笨的方法，不推荐)
    (LeetCode 提交可以通过)
    相邻赋值法，需要先从左上角遍历到右下角逐个空格赋值，再从右下角到左上角调整已有的值.
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return matrix
        # 矩阵尺寸
        m = len(matrix)
        n = len(matrix[0])
        # 可能的最远距离
        d_max = m + n - 2
        # 方向数组
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 辅助队列
        from collections import deque
        queue = deque()
        #
        ret = [[None for _ in range(n)] for _ in range(m)]
        total = m * n
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    ret[x][y] = 0
                    total -= 1
                    pass
                pass
            pass
        """
        [1] 先从左到右、从上到下，把空格填满
        """
        while total != 0:
            # 每次遍历，处理一些跟已有值相邻的格子
            for i in range(m):
                for j in range(n):
                    # 针对一个点 (i, j)
                    # print i, j
                    if ret[i][j] is None:
                        neighbor_values = []
                        for direction in directions:
                            ii = i + direction[0]
                            jj = j + direction[1]
                            if 0<=ii<=m-1 and \
                                    0<=jj<=n-1 and \
                                    ret[ii][jj] is not None:
                                neighbor_values.append(ret[ii][jj])
                                pass
                            pass
                        if neighbor_values:
                            ret[i][j] = min(neighbor_values) + 1
                            total -= 1
                            # print ret
                            pass
                        pass
                    pass
                pass
            pass

        """
        [2] 再从右到左、从下到上，调整非零空格的值
        """
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # 针对一个点 (i, j)
                # print i, j
                if ret[i][j] != 0:
                    neighbor_values = []
                    for direction in directions:
                        ii = i + direction[0]
                        jj = j + direction[1]
                        if 0<=ii<=m-1 and 0<=jj<=n-1:
                            neighbor_values.append(ret[ii][jj])
                            pass
                        pass
                    if neighbor_values:
                        ret[i][j] = min(neighbor_values) + 1
                        total -= 1
                        # print ret
                        pass
                    pass
                pass
            pass
        return ret

# ================================================================================


"""
思路:
    Flood Fill
    (BFS)
    (求最短路径，首先应该想到使用 BFS，然后是与之相配的 queue 数据结构。)
方法:
    以所有的0为起点遍历矩阵，离0越远的点，元素值逐渐增加。
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return matrix
        # 矩阵尺寸
        m = len(matrix)
        n = len(matrix[0])
        # 方向数组
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 辅助队列
        from collections import deque
        queue = deque()
        # 结果矩阵初始化
        ret = [[None for _ in range(n)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    ret[x][y] = 0
                    # 值为 0 的点，入队列
                    queue.append([x, y])  # !!!!!!!!!!
                    pass
                pass
            pass
        # print ret
        # print queue
        # BFS
        while queue:
            i, j = queue.popleft()
            for direction in directions:
                ii = i + direction[0]
                jj = j + direction[1]
                if 0 <= ii <= m - 1 and \
                        0 <= jj <= n - 1 and \
                        ret[ii][jj] is None:
                    ret[ii][jj] = ret[i][j] + 1
                    # print '>>>>>>>>>>>>>>>>>>>>>>>>>'
                    # print 'queue=', queue
                    # print 'current=', i, j
                    # print 'neighbor=', ii, jj
                    # for x in range(m):
                    #     print ret[x]
                    #     pass
                    # print '>>>>>>>>>>>>>>>>>>>>>>>>>'
                    # 被赋值的点，入队列
                    queue.append([ii, jj])  # !!!!!!!!!!
                    pass
                pass
            pass
        return ret


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()

# print so.updateMatrix(
#     [[0,0,0],[0,1,0],[0,0,0]]
# )

print so.updateMatrix(
    [[0,0,0],
     [0,1,0],
     [1,1,1]]
)
