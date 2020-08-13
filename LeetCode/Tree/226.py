#!/usr/bin/env python
# coding:utf-8

"""
226. 翻转二叉树

翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

"""


# ================================================================================
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# ================================================================================
"""
经典算法（递归）
    时间复杂度 O(n)
    空间复杂度 O(n)
"""
# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if not root:
#             return root
#
#         def invert(node):
#             node.left, node.right = node.right, node.left
#
#         invert(root)
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root


class Solution(object):
    def invertTree(self, root):
        """
        226. 翻转二叉树
        """
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# ================================================================================
"""
迭代法（广度优先搜索）利用队列
    时间复杂度 O(n)
    空间复杂度 O(n)
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            pass
        return root
# ================================================================================
# ================================================================================
# ================================================================================

