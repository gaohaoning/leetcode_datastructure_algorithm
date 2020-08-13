#!/usr/bin/env python
# coding:utf-8


"""
搜索方法:
    广度优先: Breadth First Search
    深度优先: Depth First Search
"""

# ================================================================================
"""
广度优先搜索(BFS)
    适用于: 树, 图
"""


def bfs(graph, start, end):
    # 队列
    queue = []
    # 集合
    visited = set()
    # 初始化
    queue.append(start)
    # 循环
    while queue:
        node = queue.popleft()
        visited.add(node)
        # process node
        print node
        # generate_related_nodes
        # nodes = generate_related_nodes(node)  # 此处需要获得 node 节点的子节点，(对于图的情况)同时还要过滤掉已经在 visited 中的节点
        nodes = node.children()
        queue.extend(nodes)
        pass
    pass

# ================================================================================
"""
深度优先搜索(DFS)
    适用于: 树, 图
"""
"""
非递归写法
    (自己实现 stack 结构)
    (一般不常用 !!!!!)
    
    递归方案
    优点：容易实现。 
    缺点：如果递归的深度太大，容易出现堆栈溢出。（这种情况下可能会希望，使用显式栈实现 DFS）
"""


"""
(具体代码见另外文件)
"""

# ================================================================================
"""
深度优先搜索(DFS)
    适用于: 树, 图
"""
"""
递归写法
    (递归结构自己实现了 stack 结构)

    当我们递归地实现 DFS 时，似乎不需要使用任何栈。
    但实际上，我们使用的是由系统提供的隐式栈，也称为调用栈（Call Stack）
"""


# visited = set()
def dfs(node, visited):
    # 记录当前节点
    visited.add(node)
    # 处理当前节点
    # ...
    # 递归
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)
            pass
        pass
    pass
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
