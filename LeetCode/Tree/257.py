#!/usr/bin/env python
# coding:utf-8

"""
257. 二叉树的所有路径
难度
简单

给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


# ================================================================================
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# ================================================================================
class Solution(object):
    def helper(self, node, branch_str):
        ret = []
        if not node.left and not node.right:
            ret.append(branch_str + '%s' % node.val)
            pass
        else:
            if node.left:
                list_left = self.helper(node.left, branch_str + '%s->' % node.val)
                ret.extend(list_left)
                pass
            if node.right:
                list_right = self.helper(node.right, branch_str + '%s->' % node.val)
                ret.extend(list_right)
                pass
        return ret

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        return self.helper(root, '')
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================

