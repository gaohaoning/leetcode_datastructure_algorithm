#!/usr/bin/env python
# coding:utf-8

"""
145. 二叉树的后序遍历
难度
困难

给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
思路:
    递归
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def postorder(self, node, path):
        if node.left:
            self.postorder(node.left, path)
            pass
        if node.right:
            self.postorder(node.right, path)
            pass
        path.append(node.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = list()
        if root:
            self.postorder(root, path)
        return path

# ================================================================================
"""
思路:
    迭代
        (调整 前序遍历 的迭代方法，得出结果后逆序输出)
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        stack.append(root)
        ret = []
        while stack:
            node = stack.pop()
            ret.append(node.val)
            """
            注意: 先压左孩子，再压右孩子!
            """
            if node.left:
                stack.append(node.left)
                pass
            if node.right:
                stack.append(node.right)
                pass
            pass
        return ret[::-1]


# ================================================================================
# ================================================================================
# ================================================================================


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7

print Solution().postorderTraversal(a1)
# [4, 5, 2, 6, 7, 3, 1]
