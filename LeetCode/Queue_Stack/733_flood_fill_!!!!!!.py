#!/usr/bin/env python
# coding:utf-8

"""
733. 图像渲染
难度
简单

有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

示例 1:

输入:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。
注意:

image 和 image[0] 的长度在范围 [1, 50] 内。
给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
"""
# ================================================================================
"""
思路:
    Flood Fill
    (BFS 或 DFS 都可以)
时间复杂度:
    O()
空间复杂度: 
    O()
"""
# ================================================================================

"""
DFS
"""

class Solution(object):
    def dfs(self, matrix, i, j, m, n, oldColor, newColor):
        """
        深度优先遍历
        """
        # 方向数组
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 先染色
        matrix[i][j] = newColor
        # 再递归处理邻居
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0<=new_i<=m-1 and \
                    0<=new_j<=n-1 and \
                    matrix[new_i][new_j] == oldColor:
                self.dfs(matrix, new_i, new_j, m, n, oldColor, newColor)
                pass
            pass

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        """
        注意: newColor 可能与初始值相同，此种情况要避免陷入死循环，直接返回即可不用处理。
        """
        if len(image) == 0:
            return image
        m = len(image)
        n = len(image[0])
        # DFS
        oldColor = image[sr][sc]
        if image[sr][sc] != newColor:
            self.dfs(image, sr, sc, m, n, oldColor, newColor)
            pass
        return image

# ================================================================================

"""
BFS
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        """
        注意: newColor 可能与初始值相同，此种情况要避免陷入死循环，直接返回即可不用处理。
        """
        if len(image) == 0:
            return image
        m = len(image)
        n = len(image[0])
        # 方向数组
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 辅助队列
        from collections import deque
        queue = deque()
        # BFS
        oldColor = image[sr][sc]
        if image[sr][sc] != newColor:
            # 先染色
            image[sr][sc] = newColor
            # 再入队
            queue.append([sr, sc])
            while queue:
                x, y = queue.popleft()
                for direction in directions:
                    x_new = x + direction[0]
                    y_new = y + direction[1]
                    if 0 <= x_new <= m-1 and \
                            0 <= y_new <= n-1 and \
                            image[x_new][y_new] == oldColor:
                        # 先染色
                        image[x_new][y_new] = newColor
                        # 再入队
                        queue.append([x_new, y_new])
                        pass
                    pass
                pass
            pass
        return image
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()

image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
sr = 1
sc = 1
newColor = 2

print so.floodFill(image, sr, sc, newColor)
# [[2, 2, 2],
#  [2, 2, 0],
#  [2, 0, 1]]
