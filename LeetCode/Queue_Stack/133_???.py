#!/usr/bin/env python
# coding:utf-8

"""
133. 克隆图
难度
中等

给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值 val（Int） 和其邻居的列表（list[Node]）。

示例：



输入：
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

解释：
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。


提示：

节点数介于 1 到 100 之间。
无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
必须将给定节点的拷贝作为对克隆图的引用返回。
"""
# ================================================================================
# TODO: 有待理解 ？？？？？？？？？？？？？？？？？？？？

"""
思路:
    DFS:
        无向连通图的搜索，
        用dfs遍历整个图，并为每个节点创建副本到哈希表，
        当回溯之时，所有节点已经在表中，修改邻居即可。
时间复杂度:
    O()
空间复杂度: 
    O()
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 维护一个哈希表
        d = {}

        def dfs(old):
            if old not in d:
                # 每遍历一个节点就创建一个它的副本到哈希表
                new = Node(old.val, None)
                d[old] = new
                # 当所有节点进入哈希表之时开始回溯，修改邻居
                new.neighbors = map(dfs, old.neighbors)
            return d[old]

        return dfs(node)

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================