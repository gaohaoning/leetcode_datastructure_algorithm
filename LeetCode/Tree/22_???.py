#!/usr/bin/env python
# coding:utf-8

"""
22. 括号生成

给出 n 代表生成括号的对数， 组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
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
覃超解法(没有完全理解 ?????)
"""
class Solution(object):
    def _gen(self, left, right, n, result):
        """
        :param left: 左括号已经用了几个
        :param right: 右括号已经用了几个
        :param n: 种数
        :param result: 当前产生的括号序列
        :return: 生成的序列(字符串)
        """
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left + 1, right, n, result + '(')
        if right < n and right < left:
            self._gen(left, right + 1, n, result + ')')

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, '')
        return self.list
# ================================================================================
"""
Approach 2: Backtracking
Intuition and Algorithm
Instead of adding '(' or ')' every time as in Approach 1, 
let's only add them when we know it will remain a valid sequence. 
We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place. 
And we can start a closing bracket if it would not exceed the number of opening brackets.


Time Complexity : O(4**n/sqrt(n))
    Each valid sequence has at most n steps during the backtracking procedure.

Space Complexity : O(4**n/sqrt(n))
    as described above, and using O(n)O(n) space to store the sequence. 

"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ret.append(s)
                pass
            if left < n:
                backtrack(s + '(', left + 1, right)
                pass
            if right < left:
                backtrack(s + ')', left, right + 1)
                pass
            pass

        backtrack('', 0, 0)
        return ret

# ================================================================================
# ================================================================================
# ================================================================================

