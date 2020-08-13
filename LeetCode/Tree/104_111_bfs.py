#!/usr/bin/env python
# coding:utf-8

"""
二叉树的 最大深处 & 最小深度
"""


"""
104. 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


"""
111. 二叉树的最小深度

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


# ================================================================================
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# ================================================================================
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        #
        # result = []
        level = 0
        # 队列
        from collections import deque
        queue = deque()
        # 集合
        # visited = set()
        # 初始化
        queue.append(root)
        #
        while queue:
            # 分层处理
            level_size = len(queue)
            # current_level = []
            # 每次处理一层
            for _ in range(level_size):
                node = queue.popleft()
                # current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                pass
            # 每层一个 list
            # result.append(current_level)
            #
            level += 1
            pass
        return level
# ================================================================================
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        #
        # result = []
        level = 0
        # 队列
        from collections import deque
        queue = deque()
        # 集合
        # visited = set()
        # 初始化
        queue.append(root)
        #
        while queue:
            # 分层处理
            level_size = len(queue)
            # current_level = []
            # 每次处理一层
            for _ in range(level_size):
                node = queue.popleft()
                # current_level.append(node.val)
                # 判断是否为叶子节点
                if not node.left and not node.right:
                    return level + 1
                #
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                pass
            # 每层一个 list
            # result.append(current_level)
            #
            level += 1
            pass
# ================================================================================
# ================================================================================

