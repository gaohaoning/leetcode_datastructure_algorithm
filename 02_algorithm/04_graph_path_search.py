#!/usr/bin/env python
# coding:utf-8

"""
有向图
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
# 查找一条路径
def find_path(graph, start, stop, path=None):
    if not path:
        path = []
    path = path + [start]
    if start == stop:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, stop, path)
            if new_path:
                return new_path
    return None
print '----------------------------------------------------------------------------------------------------'
print find_path(graph, a, e)
# ['A', 'C', 'E']
print find_path(graph, b, e)
# ['B', 'C', 'E']
print '----------------------------------------------------------------------------------------------------'
# 查找所有路径
def find_path_all(graph, start, stop, path=None):
    if not path:
        path = []
    path = path + [start]
    if start == stop:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_path_all(graph, node, stop, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths
print '----------------------------------------------------------------------------------------------------'
print find_path_all(graph, a, e)
# [['A', 'C', 'E'],
#  ['A', 'C', 'D', 'E'],
#  ['A', 'B', 'C', 'E'],
#  ['A', 'B', 'C', 'D', 'E'],
#  ['A', 'B', 'D', 'E']]
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
