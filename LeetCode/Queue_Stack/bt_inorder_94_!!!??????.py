#!/usr/bin/env python
# coding:utf-8

"""
94. 二叉树的中序遍历
难度
中等

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
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
    def inorder(self, node, path):
        if node.left:
            self.inorder(node.left, path)
            pass
        path.append(node.val)
        if node.right:
            self.inorder(node.right, path)
            pass

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = list()
        if root:
            self.inorder(root, path)
        return path

# ================================================================================
# TODO: 尚未完全理解 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""
思路:
    迭代
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


# 带注释的代码


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        # stack.append(root)
        ret = []
        # node 作为指针
        node = root
        """
        注意: 
        循环条件: 指针不为空 或 栈不为空
        """
        while node or stack:
            # 左子树入栈
            while node:
                stack.append(node)
                print 'stack add: ', [n.val for n in stack]
                node = node.left
                pass
            # 弹出栈顶
            node = stack.pop()
            print 'stack pop: ', [n.val for n in stack]
            ret.append(node.val)
            print '==================== ret: ', ret
            # 看右子树
            node = node.right
            pass
        return ret


# 无注释的代码


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        ret = []
        node = root
        """
        注意: 
        循环条件: 指针不为空 或 栈不为空
        """
        while node or stack:
            # 左子树入栈
            while node:
                stack.append(node)
                node = node.left  # !!!!!!!!!!!!
                pass
            # 弹出栈顶
            node = stack.pop()
            # 处理栈顶
            ret.append(node.val)
            # 看右子树
            node = node.right  # !!!!!!!!!!!!
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

print Solution().inorderTraversal(a1)
# [4, 2, 5, 1, 6, 3, 7]
