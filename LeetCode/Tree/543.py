#!/usr/bin/env python
# coding:utf-8

"""
543. 二叉树的直径
难度
简单

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
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
递归法

二叉树的直径 = max(经过根节点的左右子树最大深度之和，左子树的直径，右子树的直径)
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
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        diameter = depth_left + depth_right
        return max(
            diameter,
            max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        )

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

