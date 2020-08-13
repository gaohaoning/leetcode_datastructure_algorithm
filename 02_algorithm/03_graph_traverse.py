#!/usr/bin/env python
# coding:utf-8

"""
有向图遍历
"""
print '----------------------------------------------------------------------------------------------------'
a, b, c, d, e = 'A', 'B', 'C', 'D', 'E'

# 邻接表
graph = {
    a: {b, c},
    b: {c, d},
    c: {d, e},
    d: {e},
    e: {},
}
print graph
# {'A': set(['C', 'B']), 'C': set(['E', 'D']), 'B': set(['C', 'D']), 'E': {}, 'D': set(['E'])}

# 顶点数组
vertexes = [a, b, c, d, e]
print vertexes
# ['A', 'B', 'C', 'D', 'E']

# 邻接矩阵
matrix = []
for node1 in vertexes:
    list_node = []
    for node2 in vertexes:
        if node1 in graph and node2 in graph[node1]:
            list_node.append(1)
        else:
            list_node.append(0)
    matrix.append(list_node)
print matrix
# [[0, 1, 1, 0, 0],
#  [0, 0, 1, 1, 0],
#  [0, 0, 0, 1, 1],
#  [0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0]]
print '----------------------------------------------------------------------------------------------------'
"""
深度优先遍历 DFS
(递归，使用stack)
"""

visited = {}.fromkeys(graph.keys(), False)

def traverse_dfs(graph, start):
    visited[start] = True
    path = [start]
    for node in graph[start]:
        if not visited[node]:
            visited[node] = True
            new_path = traverse_dfs(graph, node)
            path.extend(new_path)
    return path

print traverse_dfs(graph, a)
# ['A', 'C', 'E', 'D', 'B']
print '----------------------------------------------------------------------------------------------------'
"""
广度优先遍历 BFS
(使用 queue)
"""

visited = {}.fromkeys(graph.keys(), False)

def traverse_bfs(graph, start):
    visited[start] = True
    path = [start]
    queue = [start]
    while queue:
        for node in graph[queue[0]]:
            if not visited[node]:
                visited[node] = True
                path.append(node)
                queue.append(node)
        queue.pop(0)
    return path

print traverse_bfs(graph, a)
# ['A', 'C', 'B', 'E', 'D']
print '----------------------------------------------------------------------------------------------------'
