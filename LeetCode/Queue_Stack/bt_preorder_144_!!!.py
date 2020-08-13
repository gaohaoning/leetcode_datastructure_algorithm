#!/usr/bin/env python
# coding:utf-8

"""
144. 二叉树的前序遍历
难度
中等

给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
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
    O()
空间复杂度: 
    O()
"""


class Solution(object):
    def preorder(self, node, path):
        path.append(node.val)
        if node.left:
            self.preorder(node.left, path)
            pass
        if node.right:
            self.preorder(node.right, path)
            pass

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = list()
        if root:
            self.preorder(root, path)
        return path


# ================================================================================
"""
思路:
    迭代
        (从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，先压右孩子再压左孩子。)
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""

"""
迭代处理步骤:
    处理 node
    入栈 node.right
    入栈 node.left
"""


# 带注释的代码


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        stack.append(root)
        print 'stack add: ', [n.val for n in stack]
        ret = []
        while stack:
            node = stack.pop()
            print 'stack pop: ', [n.val for n in stack]
            ret.append(node.val)
            print '==================== ret: ', ret
            """
            注意: 先压右孩子，再压左孩子!
            """
            if node.right:
                stack.append(node.right)
                print 'stack add: ', [n.val for n in stack]
                pass
            if node.left:
                stack.append(node.left)
                print 'stack add: ', [n.val for n in stack]
                pass
            pass
        return ret


# 无注释的代码


class Solution(object):
    def preorderTraversal(self, root):
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
            注意: 先压右孩子，再压左孩子!
            """
            if node.right:
                stack.append(node.right)
                pass
            if node.left:
                stack.append(node.left)
                pass
            pass
        return ret


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

print Solution().preorderTraversal(a1)
# [1, 2, 4, 5, 3, 6, 7]
