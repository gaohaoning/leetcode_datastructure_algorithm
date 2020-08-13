#!/usr/bin/env python
# coding:utf-8

"""
200. 岛屿数量
难度
中等

给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
"""
# ================================================================================
"""
洪水填充算法(Flood Fill Algorithm)
"""
"""
Flood Fill 算法

是从一个区域中提取若干个连通的点与其他相邻区域区分开（或分别染成不同颜色）的经典算法。
因为其思路类似洪水从一个区域扩散到所有能到达的区域而得名。

从一个点扩散开，找到与其连通的点，这不是什么高深的算法，
其实就是从一个点开始，进行一次“深度优先遍历”或者“广度优先遍历”，
通过“深度优先遍历”或者“广度优先遍历”发现一片连着的区域，

对于这道题来说，
就是从一个是“陆地”的格子开始进行一次“深度优先遍历”或者“广度优先遍历”，
把与之相连的所有的格子都标记上，视为发现了一个“岛屿”。

说明：
那么每一次进行“深度优先遍历”或者“广度优先遍历”的条件就是：
1、这个格子是陆地（“1”），如果是水域（“0”）就无从谈论“岛屿”；
2、这个格子不能是之前发现“岛屿”的过程中执行了“深度优先遍历”或者“广度优先遍历”操作，而被标记的格子。
"""
# ================================================================================
"""
思路:
    DFS(深度优先遍历)
    (回溯)
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量
    """
           x-1,y
    x,y-1    x,y    x,y+1
           x+1,y
    """
    # 这4个方向的顺序无关紧要
    # 此处的方向顺序：上、右、下、左
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(self, matrix, i, j, m, n, visited):
        """
        深度优先遍历
        """
        visited[i][j] = True
        # print '(%s,%s)' % (i, j)
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            """
            对下一个格子，执行 DFS 的条件:
            1.横坐标在网格内
            2.纵坐标在网格内
            3.该格子没有被遍历过
            4.该格子是陆地
            """
            if 0<=new_i<=m-1 \
                    and 0<=new_j<=n-1 \
                    and not visited[new_i][new_j] \
                    and matrix[new_i][new_j] == '1':
                self.dfs(matrix, new_i, new_j, m, n, visited)
                pass
            pass

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        # 孤岛计数
        island_count = 0
        # 已访问过的记录矩阵
        matrix_visited = [[False for _ in range(n)] for _ in range(m)]
        """
        从 (0,0) 开始，对每个格子尝试一次 DFS 操作
        """
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if grid[i][j] == '1' and not matrix_visited[i][j]:
                    self.dfs(grid, i, j, m, n, matrix_visited)
                    # 岛屿计数 +1  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    island_count += 1
                    # print 'island_count:', island_count
                    pass
                pass
            pass
        return island_count

# ================================================================================
"""
思路:
    BFS(广度优先遍历)
    (需要一个辅助队列)
时间复杂度:
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量
    """
           x-1,y
    x,y-1    x,y    x,y+1
           x+1,y
    """
    # 这4个方向的顺序无关紧要
    # 此处的方向顺序：上、右、下、左
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        # 孤岛计数
        island_count = 0
        # 已访问过的记录矩阵
        matrix_visited = [[False for _ in range(n)] for _ in range(m)]
        # 辅助队列
        from collections import deque
        queue = deque()
        """
        从 (0,0) 开始，对每个格子尝试一次 BFS 操作
        """
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
                if grid[i][j] == '1' and not matrix_visited[i][j]:
                    # ------------------------------
                    # 岛屿计数 +1  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    island_count += 1
                    # print 'island_count: ', island_count
                    matrix_visited[i][j] = True
                    # print '(%s,%s)' % (i, j)
                    queue.append((i, j))
                    # ------------------------------
                    while queue:
                        x, y = queue.popleft()
                        # 依次检查 4 个方向的邻居
                        for direction in self.directions:
                            new_i = x + direction[0]
                            new_j = y + direction[1]
                            """
                            标记该格子已被访问，并且入队列的条件:
                            1.横坐标在网格内
                            2.纵坐标在网格内
                            3.该格子没有被遍历过
                            4.该格子是陆地
                            """
                            if 0 <= new_i <= m - 1 \
                                    and 0 <= new_j <= n - 1 \
                                    and not matrix_visited[new_i][new_j] \
                                    and grid[new_i][new_j] == '1':
                                # 标记已访问
                                matrix_visited[new_i][new_j] = True
                                # print '(%s,%s)' % (new_i, new_j)
                                # 加入队列
                                queue.append((new_i, new_j))
                            pass
                        pass
                    # ------------------------------
                    pass
                pass
            pass
        return island_count


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


gggg = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']]
solution = Solution()
result = solution.numIslands(gggg)
print(result)
