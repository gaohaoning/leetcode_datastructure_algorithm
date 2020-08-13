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
"""
分治算法
递归
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # ============================== 递归终止条件
        if not root:
            return 0
        # ============================== 分割问题
        # ============================== 解决子问题
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        # ============================== 合并结果
        return 1 + max(left_max, right_max)

# ================================================================================
"""
分治算法
递归
"""
# class Solution(object):
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         # ============================== 递归终止条件
#         if not root:
#             return 0
#         # ============================== 分割问题
#         # ============================== 解决子问题
#         """
#         由于存在节点没有左子树或右子树的情况，所以不能直接求: 最小深度+1
#         """
#         if not root.left:
#             return 1 + self.minDepth(root.right)
#         if not root.right:
#             return 1 + self.minDepth(root.left)
#         """
#         保证节点同时存在左子树和右子树的情况，可以直接求: 最小深度+1
#         """
#         left_min = self.minDepth(root.left)
#         right_min = self.minDepth(root.right)
#         # ============================== 合并结果
#         result = 1 + min(left_min, right_min)
#         return result


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # ============================== 递归终止条件
        if not root:
            return 0
        # ============================== 分割问题
        # ============================== 解决子问题
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        # ============================== 合并结果
        if left_min == 0:
            return 1 + right_min
        elif right_min == 0:
            return 1 + left_min
        else:
            return 1 + min(left_min, right_min)

# ================================================================================
# ================================================================================

