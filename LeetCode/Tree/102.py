#!/usr/bin/env python
# coding:utf-8

"""
102. 二叉树的层次遍历

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""


# ================================================================================
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
方法1: 广度优先遍历(需要特殊处理每一层)

复杂度:
    时间: O(n)
    空间: O(n)
"""
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        #
        result = []
        # 队列
        queue = deque()
        # 集合
        # visited = set()
        # 初始化
        queue.append(root)
        #
        while queue:
            # 分层处理
            level_size = len(queue)
            current_level = []
            # 每次处理一层
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                pass
            # 每层一个 list
            result.append(current_level)
            pass
        return result


"""
方法2: 深度优先遍历(此法属于炫技)

思路:
    先逐层把需要的 list 建好，然后用深度优先算法，依次向对应的层的 list 中添加元素

复杂度:
    时间: O(?)
    空间: O(?)
"""
class Solution(object):
    def dfs(self, node, level):
        """
        深度优先遍历 node，将遍历到的节点值存入 result 二维数组中对应的位置
        """
        # ============================== 递归终止条件
        if not node:
            return
        # ============================== 当前层级的处理逻辑
        if len(self.result) < level + 1:
            self.result.append([])
            pass
        self.result[level].append(node.val)
        # ============================== 递归调用
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)
        # ============================== 收尾工作
        return

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        #
        self.result = []  # 二维数组
        self.dfs(root, 0)  # 第0层
        return self.result
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

