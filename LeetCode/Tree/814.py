#!/usr/bin/env python
# coding:utf-8

"""
814. 二叉树剪枝
难度
中等

给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

返回移除了所有不包含 1 的子树的原二叉树。

( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

示例1:
输入: [1,null,0,0,1]
输出: [1,null,0,null,1]

解释:
只有红色节点满足条件“所有不包含 1 的子树”。
右图为返回的答案。


示例2:
输入: [1,0,1,0,0,0,1]
输出: [1,null,1,null,1]



示例3:
输入: [1,1,0,1,1,0,1,0]
输出: [1,1,0,1,1,null,1]



说明:

给定的二叉树最多有 100 个节点。
每个节点的值只会为 0 或 1 。
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
    Time Complexity: O(N)
        where N is the number of nodes in the tree. We process each node once.
    Space Complexity: O(H)
        where H is the height of the tree.
        This represents the size of the implicit call stack in our recursion.
"""
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def containsOne(node):
            """
            containsOne(node) does two things:
                [1] it tells us whether the subtree at this node contains a 1,
                [2] and it also prunes all subtrees not containing 1.
            """
            if node is None:
                return False
            left = containsOne(node.left)
            right = containsOne(node.right)
            if not left:
                node.left = None  # prune
            if not right:
                node.right = None  # prune
            return bool(node.val) or left or right

        return root if containsOne(root) else None

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

