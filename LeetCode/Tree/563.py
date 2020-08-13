#!/usr/bin/env python
# coding:utf-8

"""
563. 二叉树的坡度
难度
简单

给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

示例:

输入:
         1
       /   \
      2     3
输出: 1
解释:
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
注意:

任何子树的结点的和不会超过32位整数的范围。
坡度的值不会超过32位整数的范围。
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
方法1: 递归（效率较低）
"""
class Solution(object):
    def sum(self, node):
        if not node:
            return 0
        left = self.sum(node.left)
        right = self.sum(node.right)
        return node.val + left + right
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        t_left = self.findTilt(root.left)
        t_right = self.findTilt(root.right)
        t = t_left + t_right + abs(self.sum(root.left) - self.sum(root.right))
        return t

# ================================================================================
"""
方法2: 后序遍历（postorder）
"""
class Solution(object):
    """
    这里用一个 类属性 存储累加的坡度值
    """
    ret = 0
    def postorder(self, node):
        if not node:
            return 0
        left_sum = self.postorder(node.left)
        right_sum = self.postorder(node.right)
        self.ret += abs(left_sum - right_sum)
        return node.val + left_sum + right_sum
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.postorder(root)
        return self.ret

# ================================================================================
# ================================================================================
# ================================================================================

