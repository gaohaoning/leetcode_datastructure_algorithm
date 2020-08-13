#!/usr/bin/env python
# coding:utf-8

"""
98. 验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""


# ================================================================================
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
方法1：中序遍历后排序（效率较低）
"""
class Solution(object):
    def inorder(self, root):
        """
        中序遍历
        """
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        inorder = self.inorder(root)
        # print inorder
        # print list(sorted(inorder))
        # print inorder == sorted(inorder)
        # print inorder == list(sorted(inorder))
        # print inorder == list(sorted(set(inorder)))
        # return inorder == list(sorted(inorder))
        # 此处需要处理成 set，因为BST要求孩子节点跟父节点的关系必须是小于和大于，不允许有等于的情况。
        # set 可以将值相等的节点去重
        return inorder == list(sorted(set(inorder)))


# ================================================================================
"""
方法2：
递归判断
    注意：
        BST 要求根节点左/右子树所有节点的值小于/大于根节点的值，
        所以逐个节点遍历时只比较每个根节点和左右孩子节点是不够的！
        必须通过极限值加以检查！
    例如：
        10
       / \
      5   15
         / \
        6   20

Complexity Analysis
    Time complexity : O(N) since we visit each node exactly once.
    Space complexity : O(N) since we keep up to the entire tree.
"""
class Solution(object):
    def isValid(self, node, vmin, vmax):
        # 注意 节点值可能为零，所以用作判断时不能直接用来做 bool 型判断，必须用 x is not None
        if vmin is not None and vmin >= node.val:
            return False
        if vmax is not None and vmax <= node.val:
            return False
        ret_left = self.isValid(node.left, vmin, node.val) if node.left else True
        ret_right = self.isValid(node.right, node.val, vmax) if node.right else True
        return ret_left and ret_right

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isValid(root, None, None)

# ================================================================================
"""
方法3：
Iteration
    The above recursion could be converted into iteration, with the help of stack. 
    DFS would be better than BFS since it works faster here.
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = [(root, None, None), ]
        while stack:
            node, low, high = stack.pop()
            if node.left:
                if node.left.val >= node.val:
                    return False
                if low and node.left.val <= low:
                    return False
                stack.append((node.left, low, node.val))
            if node.right:
                if node.right.val <= node.val:
                    return False
                if high and node.right.val >= high:
                    return False
                stack.append((node.right, node.val, high))
        return True


# ================================================================================
# ================================================================================
root = TreeNode(1)
right = TreeNode(1)
root.right = right

so = Solution()
print so.isValidBST(root)

