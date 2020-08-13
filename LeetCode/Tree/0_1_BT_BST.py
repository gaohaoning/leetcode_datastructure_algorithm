#!/usr/bin/env python
# coding:utf-8

"""
Tree
"""

# ================================================================================
"""
Binary Tree
(二叉树)
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        pass
    pass


# ================================================================================
"""
Binary Search Tree
(二叉搜索树、二叉查找树、二叉排序树)

    它或者是一棵空树，
    或者是具有下列性质的二叉树： 
        1.若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
        2.若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
        3.它的左、右子树也分别为二叉排序树。
"""
# ================================================================================
"""
DFS(深度优先搜索)
    3种遍历方式:
        preorder: 前序
            [根] 左 右
        inorder: 中序 
            左 [根] 右
        postorder: 后序 
            左 右 [根]
"""


class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        self.traverse_path = []
        pass

    def preorder(self, node):
        if node:
            self.traverse_path.append(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.traverse_path.append(node.val)
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            self.traverse_path.append(node.val)


# ================================================================================
# ================================================================================

