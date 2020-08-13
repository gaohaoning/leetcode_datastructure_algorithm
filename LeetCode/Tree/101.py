#!/usr/bin/env python
# coding:utf-8

"""
101. 对称二叉树
难度
简单

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
笨方法: 翻转(递归)、对比(递归)
"""
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

    def isSame(self, a, b):
        if a is None or b is None:
            return a == b
        if a.val != b.val:
            return False
        if not self.isSame(a.left, b.left) or not self.isSame(a.right, b.right):
            return False
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.invertTree(root.left)
        return self.isSame(root.left, root.right)
# ================================================================================
"""
递归法(recursion)
    Time complexity : O(n)
    Space complexity : O(n) （in the worst case）
"""
class Solution(object):
    def isMirror(self, a, b):
        if a is None or b is None:
            return a == b
        return a.val == b.val and self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

# ================================================================================
"""
迭代法(iteration)
    Time complexity : O(n)
    Space complexity : O(n) （in the worst case）
"""
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left, right = queue.popleft(), queue.popleft()
            if left is None or right is None:
                if left is right:
                    continue
                else:
                    return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
            pass
        return True

# ================================================================================
# ================================================================================

